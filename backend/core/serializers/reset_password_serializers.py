from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from ..models import User, PasswordResetToken
from ..utils import send_reset_password_email


class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create_reset_token(self, validated_data):
        email = validated_data.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with the given email not found")

        token = PasswordResetToken.objects.create(user=user)
        send_reset_password_email(email, token.token)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        return value

    def save(self, user):
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
