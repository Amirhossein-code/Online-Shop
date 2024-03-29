from django.contrib import admin
from ..models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "unit_price",
        "inventory",
        "category",
        "created_at",
        "last_update",
    ]
    list_filter = ["category", "created_at", "last_update"]
    search_fields = ["title", "description"]

    fieldsets = (
        (
            None,
            {"fields": ("title", "unit_price", "inventory", "category", "description")},
        ),
    )

    readonly_fields = ("created_at", "last_update")


