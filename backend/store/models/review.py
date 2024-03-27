from django.db import models
from ..models import Customer, Product
from common.validators import validate_rating


class ProductReview(models.Model):

    PENDING = "pending"
    APPROVED = "approved"
    NOT_APPROVED = "not_approved"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (NOT_APPROVED, "Not Approved"),
    ]

    rating = models.FloatField(validators=[validate_rating])
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="review",
    )
