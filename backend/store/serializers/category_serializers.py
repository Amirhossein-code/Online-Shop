from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = [
            "id",
            "title",
            "slug",
            "description",
            "image",
        ]
        read_only_fields = [
            "id",
        ]
