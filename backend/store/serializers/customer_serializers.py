from rest_framework import serializers
from ..models import Customer


class UpdateCustomerSerializer(serializers.ModelSerializer):
    """
    For Updating Customer
    """

    class Meta:
        model = Customer
        fields = [
            "phone",
            "birth_date",
            "image",
        ]


class DetailedCustomerSerializer(serializers.ModelSerializer):
    """
    For editing the User related fields use the user endpoint provided
    """

    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "email",
            "birth_date",
            "phone",
            "joined_at",
            "last_updated",
            "image",
        ]
        read_only_fields = [
            "id",
            "email",
            "birth_date",
            "phone",
            "joined_at",
            "last_updated",
            "image",
        ]
