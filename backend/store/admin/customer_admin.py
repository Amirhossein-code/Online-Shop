from django.contrib import admin
from ..models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "phone",
        "birth_date",
        "joined_at",
        "last_updated",
    ]
    list_filter = ["joined_at", "last_updated"]
    search_fields = ["phone", "user"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "phone",
                    "birth_date",
                    "image",
                )
            },
        ),
    )

    readonly_fields = ("joined_at", "last_updated", "id")
