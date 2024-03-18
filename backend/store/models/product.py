from django.db import models
from autoslug import AutoSlugField
from common.utils import custom_slugify, round_to_nearest_thousand
from .category import Category
from ..validators import validate_file_size

class Product(models.Model):
    title = models.CharField(max_length=255)
    unit_price = models.PositiveBigIntegerField()
    inventory = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product_category",
    )

    description = models.TextField(null=True, blank=True)
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        blank=True,
        null=True,
        slugify=custom_slugify,
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="store/images", validators=[validate_file_size])
