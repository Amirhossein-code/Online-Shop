from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            "id",
            "title",
            "slug",
            "unit_price",
            "inventory",
            "description",
            "category",
        ]
        read_only_fields = [
            "id",
        ]
