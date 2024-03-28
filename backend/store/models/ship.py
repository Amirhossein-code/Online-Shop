from django.db import models
from ..models import Order, Address, Customer, OrderItem


class Ship(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE
    )  # Assuming you have an Address model

    is_shipped = models.BooleanField(default=False)

    def total_price(self):
        return sum(item.quantity * item.unit_price for item in self.order_items.all())
