from django.db import models
from autoslug import AutoSlugField
from common.utils import custom_slugify
from .category import Category
from common.validators import validate_file_size


class Product(models.Model):
    NEW_ARRIVAL = "New Arrival"
    OUT_OF_STOCK = "Out of Stock"
    AVAILABLE = "Available"
    NOT_AVAILABLE = "Not Available"
    DISCOUNTED = "Discounted"
    STATUS_CHOICES = [
        (NEW_ARRIVAL, "New Arrival"),
        (OUT_OF_STOCK, "Out of Stock"),
        (AVAILABLE, "Available"),
        (NOT_AVAILABLE, "Not Available"),
        (DISCOUNTED, "Discounted"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        blank=True,
        null=True,
        slugify=custom_slugify,
    )

    discount_percent = models.IntegerField(null=True, blank=True, default=0)
    original_price = models.PositiveBigIntegerField(null=True, blank=True)
    unit_price = models.PositiveBigIntegerField()
    inventory = models.PositiveIntegerField(default=0)

    is_hot = models.BooleanField(default=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product_category",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=NEW_ARRIVAL
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.discount_percent:
            self.original_price = self.unit_price
            discount_amount = (self.discount_percent / 100) * self.unit_price
            self.unit_price -= discount_amount
            self.status = self.DISCOUNTED
        else:
            self.original_price = None
            self.status = self.AVAILABLE
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="store/images", validators=[validate_file_size])
