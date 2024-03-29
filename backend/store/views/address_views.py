from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework import status
from ..models import Address
from ..serializers import (
    AddressSerializer,
)
from ..permissions import IsObjectOwner
from ..filters import AddressFilter
from ..paginations import NormalPagination


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AddressFilter
    pagination_class = NormalPagination

    def get_queryset(self):
        customer = self.request.user.customer
        return Address.objects.filter(customer=customer)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    @action(
        detail=False,
        methods=["GET"],
        url_path="main-address",
    )
    def main_address(self, request):
        try:
            main_address = Address.objects.get(
                customer=request.user.customer, main=True
            )
        except Address.DoesNotExist:
            return Response(
                {"detail": "Main address not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(main_address)
        return Response(serializer.data)
