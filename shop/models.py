import random
import string

from django.db import models
from django.utils.text import slugify
from django.urls import reverse


def rand_slug():
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))


class Category(models.Model):
    """
    Model representing a category.

    Attributes:
        name (str): The name of the category.
        parent (Category): The parent category.
        slug (str): The URL slug of the category.
        created_at (datetime): The date and time of creation.

    """
    name = models.CharField(max_length=250, db_index=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True
    )
    slug = models.SlugField("URL", max_length=250, unique=True, null=False, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (["slug", "parent"])
        verbose_name_plural = "categories"

    def __str__(self):
        """
        Returns a string representation of the object in hierarchical style
        """
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " > ".join(full_path[::-1])

    def save(self, *args, **kwargs):
        """
        Save the current instance to the database.
        """

        if not self.slug:
            self.slug = slugify(rand_slug() + '-pickBetter' + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shop:category-list", args=[str(self.slug)])


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", blank=True, null=True
    )
    title = models.CharField(max_length=250,)
    brand = models.CharField(max_length=250,)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, unique=True, null=False, editable=True)
    price = models.DecimalField("price", max_digits=12, decimal_places=2, default=99.99)
    image = models.ImageField(upload_to="products/products/%Y/%m/%d")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[str(self.slug)])


class ProductManager(models.Manager):

    def get_queryset(self):
        """
        Returns a queryset of products that are available.
        """
        return super(ProductManager, self).get_queryset().filter(available=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True
