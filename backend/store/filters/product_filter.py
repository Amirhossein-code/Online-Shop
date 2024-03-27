import django_filters
from ..models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "title": ["icontains"],
            "category": ["exact"],
            "status": ["exact"],
            "unit_price": ["gte", "lte"],
            "inventory": ["gte", "lte"],
            "is_hot": ["exact"],
        }
