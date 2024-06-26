from django.contrib import admin
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image", "created_at", "last_update"]
    list_filter = ["created_at", "last_update"]
    search_fields = ["title", "description"]

    fieldsets = ((None, {"fields": ("title", "description", "image")}),)

    readonly_fields = ("created_at", "last_update", "slug")
