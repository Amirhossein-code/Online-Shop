from django.contrib import admin
from ..models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "first_name",
        "last_name",
        "phone",
        "birth_date",
        "joined_at",
        "last_updated",
    ]
    list_filter = ["joined_at", "last_updated"]
    search_fields = ["first_name", "last_name", "phone"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "first_name",
                    "last_name",
                    "phone",
                    "birth_date",
                    "image",
                )
            },
        ),
    )

    readonly_fields = ("joined_at", "last_updated")

    def save_model(self, request, obj, form, change):
        obj.save()
