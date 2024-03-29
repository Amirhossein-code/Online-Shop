from rest_framework import serializers
from ..models import Discount


class DisocuntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [
            "id",
            "code",
            "percentage",
            "minimum_cart_price",
            "currency_discount_applied",
            "public",
        ]
