import django_filters
from ..models import Address


class AddressFilter(django_filters.FilterSet):
    province = django_filters.CharFilter(
        lookup_expr="icontains", label="Province contains"
    )
    city = django_filters.CharFilter(lookup_expr="icontains", label="City contains")

    class Meta:
        model = Address
        fields = [
            "province",
            "city",
        ]
