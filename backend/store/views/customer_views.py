from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework import status
from ..models import Customer
from ..serializers import (
    SimpleCustomerSerializer,
    DetailedCustomerSerializer,
    UpdateCustomerSerializer,
)
from ..permissions import IsOwner


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = SimpleCustomerSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == "me":
            if self.request.method == "PUT":
                return UpdateCustomerSerializer
            if self.request.method == "GET":
                return DetailedCustomerSerializer

        return super().get_serializer_class()

    @action(
        detail=False,
        methods=["GET", "PUT"],
        permission_classes=[IsAuthenticated, IsOwner],
    )
    def me(self, request):
        customer = self.get_object()

        if request.method == "GET":
            serializer = DetailedCustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = UpdateCustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def get_object(self):
        try:
            return Customer.objects.get(user_id=self.request.user.id)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
