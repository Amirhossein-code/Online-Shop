from rest_framework import serializers
from ..models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "phone",
            "birth_date",
            "image",
        ]


class UpdateCustomerSerializer(serializers.ModelSerializer):
    """
    For Updating Customer
    to update User fields User user endpoints provided
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
    For read_only access to customer adn user field together
    Note: For editing the User related fields use the user endpoint provided
    """

    user_id = serializers.IntegerField(source="user.id", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "user_id",
            "email",
            "username",
            "first_name",
            "last_name",
            "birth_date",
            "phone",
            "joined_at",
            "last_updated",
            "image",
        ]
        read_only_fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "birth_date",
            "phone",
            "joined_at",
            "last_updated",
            "image",
        ]
