from rest_framework import serializers
from ..models import ProductReview


# Category serialziers
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = [
            "id",
            "customer",
            "rating",
            "comment",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "product",
            "created_at",
            "customer",
        ]

    def create(self, validated_data):
        product_slug = self.context["product_slug"]
        if product_slug is None:
            raise serializers.ValidationError("product slug is required in the context")

        validated_data["product_slug"] = product_slug
        return super().create(validated_data)
