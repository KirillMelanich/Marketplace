from django.core.management.base import BaseCommand
from faker import Faker

from shop.models import Category, Product

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake products and categories"

    def create_categories(self):
        """
        Create 10 fake categories.
        """
        for _ in range(10):
            category_name = fake.word()
            parent_category = Category.objects.order_by("?").first()  # Random parent category
            category = Category.objects.create(
                name=category_name,
                parent=parent_category,
            )
            self.stdout.write(self.style.SUCCESS(f"Created Category: {category}"))

    def create_products(self):
        """
        Create 30 fake products.
        """
        for _ in range(30):
            product_title = fake.company()
            product_brand = fake.company()
            product_description = fake.paragraph(nb_sentences=2)
            product_price = fake.pydecimal(
                left_digits=3, right_digits=2, min_value=1, max_value=999.99
            )
            category = Category.objects.order_by("?").first()  # Random category
            product = Product(
                category=category,
                title=product_title,
                brand=product_brand,
                description=product_description,
                slug=fake.slug(),
                price=product_price,
                available=True,
                created_at=fake.date_time(),
                updated_at=fake.date_time(),
                discount=fake.pyint(min_value=0, max_value=20),
            )
            product.save()
            self.stdout.write(self.style.SUCCESS(f"Created Product: {product}"))

    def handle(self, *args, **options):
        # Create 10 categories
        self.create_categories()

        # Create 30 fake products
        self.create_products()

        self.stdout.write(f"Categories in DB: {Category.objects.count()}")
        self.stdout.write(f"Products in DB: {Product.objects.count()}")
