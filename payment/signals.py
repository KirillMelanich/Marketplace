from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ShippingAddress

User = get_user_model()


@receiver(post_save, sender=User)
def create_default_shipping_address(sender, instance, created, **kwargs):
    """
    Creates a default shipping address for the user if one does not already exist.

    """
    if created:
        if not ShippingAddress.objects.filter(user=instance).exists():
            ShippingAddress.create_default_shipping_address(user=instance)
