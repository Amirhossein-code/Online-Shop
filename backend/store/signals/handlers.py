from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from store.models import Customer, Product
from common.utils import round_to_nearest_thousand


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        Customer.objects.create(user=kwargs["instance"])


@receiver(pre_save, sender=Product)
def round_unit_price_of_product(sender, instance, **kwargs):
    instance.unit_price = round_to_nearest_thousand(instance.unit_price)
