from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Order, Customer
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers import (
    OrderSerializer,
    CreateOrderSerializer,
)
from ..paginations import NormalPagination
from ..filters import OrderFilter


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "post", "head", "options"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
    pagination_class = NormalPagination

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data, context={"user_id": self.request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user

        customer_id = Customer.objects.only("id").get(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)
