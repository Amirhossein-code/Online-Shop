from django.contrib import admin
from ..models import Category
from common.utils import custom_slugify


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image", "created_at", "last_update"]
    list_filter = ["created_at", "last_update"]
    search_fields = ["title", "description"]

    fieldsets = ((None, {"fields": ("title", "description", "image")}),)

    readonly_fields = ("created_at", "last_update")

    def save_model(self, request, obj, form, change):
        if change:
            old_category = Category.objects.get(pk=obj.pk)
            if obj.title != old_category.title:
                obj.slug = custom_slugify(obj.title)
        obj.save()
