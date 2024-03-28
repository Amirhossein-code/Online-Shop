from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "last_updated",
        ]
        read_only_fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "joined_at",
            "last_updated",
        ]


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
        ]


class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]
        read_only_fields = [
            "id",
            "username",
        ]
