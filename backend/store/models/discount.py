from django.db import models
from common.validators import percentage_validator


class Discount(models.Model):
    code = models.CharField(max_length=30)
    percentage = models.PositiveIntegerField(
        null=True, blank=True, validators=[percentage_validator]
    )
    minimum_cart_price = models.PositiveIntegerField()

    """
    If the percentage value is set this will be apply as maximum in currency  Discount 
    If it is not set the value will be deducted from the cart
    """
    currency_discount_applied = models.PositiveIntegerField()

    def __str__(self):
        return self.title
