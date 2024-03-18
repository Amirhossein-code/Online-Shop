from django.db import models
from autoslug import AutoSlugField
from common.utils import custom_slugify, round_to_nearest_thousand
from .category import Category


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
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Products"
