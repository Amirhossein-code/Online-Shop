from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from ..serializers import (
    RequestPasswordResetSerializer,
)


class RequestPasswordResetView(GenericAPIView):
    """
    When a registered user wants to set a new password because the old one is forgotten,
    they first post their email. If the email is registered, a reset password
    link with a token is emailed to the user.
    """

    serializer_class = RequestPasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.create_reset_token(serializer.validated_data)

        return Response(
            "Password reset link sent successfully. Check your email.",
            status=status.HTTP_200_OK,
        )
