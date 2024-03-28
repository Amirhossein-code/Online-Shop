from django.dispatch import Signal

order_created = Signal()

from . import create_ship_signal, handlers