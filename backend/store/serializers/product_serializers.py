from rest_framework import serializers
from ..models import Product, ProductImage


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = [
            "id",
            "title",
            "slug",
            "unit_price",
            "category",
        ]
        read_only_fields = [
            "id",
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context["product_id"]
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

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
            "images",
        ]
        read_only_fields = [
            "id",
        ]
