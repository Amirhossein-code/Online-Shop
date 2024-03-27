from rest_framework import serializers
from ..models import ProductReview, Product


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
            # "product",
            "created_at",
            "customer",
        ]

    def create(self, validated_data):
        product_slug = self.context.get("product_slug")
        if product_slug is None:
            raise serializers.ValidationError("Product slug is required in the context")

        product = Product.objects.get(slug=product_slug)
        validated_data["product"] = product
        return super().create(validated_data)


from rest_framework import serializers
from ..models import ProductReview, Product


# Category serialziers
class DisplayProductReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductReview
        fields = [
            "id",
            "username",
            "rating",
            "comment",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "username",
            "rating",
            "comment",
            "created_at",
        ]

    def get_username(self, obj):
        return obj.customer.user.display_name
