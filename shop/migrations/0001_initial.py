# Generated by Django 5.0.1 on 2024-02-01 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=250)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "unique_together": {("slug", "parent")},
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("brand", models.CharField(max_length=250)),
                ("description", models.TextField(blank=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=99.99,
                        max_digits=7,
                        verbose_name="price",
                    ),
                ),
                ("image", models.ImageField(upload_to="products/products/%Y/%m/%d")),
                ("available", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="shop.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductProxy",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("shop.product",),
        ),
    ]
