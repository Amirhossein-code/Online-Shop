import django_filters
from ..models import Order


class OrderFilter(django_filters.FilterSet):
    payment_status = django_filters.ChoiceFilter(
        choices=Order.PAYMENT_STATUS_CHOICES, label="Payment Status"
    )
    shipment_status = django_filters.ChoiceFilter(
        choices=Order.SHIPMENT_STATUS_CHOICES, label="Shipment Status"
    )

    class Meta:
        model = Order
        fields = ["payment_status", "shipment_status"]
