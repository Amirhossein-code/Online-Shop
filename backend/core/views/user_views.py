from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from ..models import User
from ..serializers import UpdateUserSerializer, UserSerializer, SimpleUserSerializer
from ..permissions import IsUserOwner


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    This view set is provided to see the current user and update it
    Note: DestroyModelmixin has been removed to not support delelte actions

    For Crating users use the register endpoint
    For reseting password user reset password end point
    """

    serializer_class = SimpleUserSerializer
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == "update":
            return UpdateUserSerializer
        if self.action == "retrieve":
            return UserSerializer
        return SimpleUserSerializer
