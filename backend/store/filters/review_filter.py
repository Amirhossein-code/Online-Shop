import django_filters
from ..models import ProductReview


class ProductReviewFilter(django_filters.FilterSet):
    rating = django_filters.NumberFilter(field_name="rating", label="Rating")
    status = django_filters.ChoiceFilter(
        choices=ProductReview.STATUS_CHOICES, label="Status"
    )

    class Meta:
        model = ProductReview
        fields = ["rating", "status"]
