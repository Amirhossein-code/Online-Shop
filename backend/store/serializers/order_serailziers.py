from rest_framework import serializers
from ..models import Order, OrderItem
from ..serializers import SimpleProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "quantity",
            "unit_price",
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "placed_at",
            "payment_status",
            "customer",
            "items",
        ]
