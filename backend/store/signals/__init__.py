from .handlers import create_customer_for_new_user, round_unit_price_of_product

from django.dispatch import Signal

order_created = Signal()
