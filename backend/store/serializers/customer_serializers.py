from rest_framework import serializers
from ..models import Customer


class UpdateCustomerSerializer(serializers.ModelSerializer):
    """
    For Updating Customer
    """

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "phone",
            "birth_date",
            "image",
        ]


class SimpleCustomerSerializer(serializers.ModelSerializer):
    """
    Simple Readonly serializer for Customer
    """

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
        ]
        read_only_fields = [
            "id",
            "first_name",
            "last_name",
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
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "phone",
            "joined_at",
            "last_updated",
            "image",
        ]
        read_only_fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "phone",
            "joined_at",
            "last_updated",
            "image",
        ]
