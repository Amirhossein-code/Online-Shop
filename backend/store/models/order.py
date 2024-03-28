from django.db import models
from ..models import Customer, Product


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]

    SHIPMENT_STATUS_NO_ORDER = "No order to set status"
    SHIPMENT_STATUS_FAILED = "Shipment failed"
    SHIPMENT_STATUS_SHIPPED = "Shipment success"
    SHIPMENT_STATUS_NOT_SHIPPED = "Order is being processed"
    SHIPMENT_STATUS_CHOICES = [
        (SHIPMENT_STATUS_NO_ORDER, "No order to set status"),
        (SHIPMENT_STATUS_FAILED, "Shipment failed"),
        (SHIPMENT_STATUS_SHIPPED, "Shipment success"),
        (SHIPMENT_STATUS_NOT_SHIPPED, "Order is being processed"),
    ]
    shipment_status = models.CharField(
        max_length=30, choices=SHIPMENT_STATUS_CHOICES, default=SHIPMENT_STATUS_NO_ORDER
    )
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="orderitems"
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.PositiveBigIntegerField()
