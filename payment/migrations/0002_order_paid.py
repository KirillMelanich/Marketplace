# Generated by Django 5.0.1 on 2024-02-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]
