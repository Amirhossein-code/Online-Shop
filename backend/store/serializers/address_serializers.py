from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "province",
            "city",
            "street",
            "full_address",
            "main",
            "customer",
        ]
        read_only_fields = [
            "id",
        ]
