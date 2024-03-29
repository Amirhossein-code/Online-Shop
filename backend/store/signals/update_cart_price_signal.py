from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import CartItem


@receiver(post_save, sender=CartItem)
@receiver(post_delete, sender=CartItem)
def update_cart_total_price(sender, instance, **kwargs):
    instance.cart.update_total_price()
