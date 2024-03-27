from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Product, ProductImage
from ..serializers import (
    ProductSerializer,
    ProductImageSerializer,
    SimpleProductSerializer,
)
from ..filters import ProductFilter


class ProductViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    Altough advanced filtering is implemented custom endpoint for retreiving
    Products is also avaiable, It has been implemented for ?
    """

    queryset = Product.objects.all()
    serializer_class = SimpleProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    lookup_field = "slug"

    def get_queryset(self):
        if self.action == "hot_list":
            return Product.objects.filter(is_hot=True).all()
        if self.action == "discounted_list":
            return Product.objects.filter(status=Product.DISCOUNTED)
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductSerializer
        return SimpleProductSerializer
    @action(
        detail=False,
        methods=["GET"],
        url_path="hot",
        permission_classes=[AllowAny],
    )
    def hot_list(self, request):
        hot_list_products = self.get_queryset()
        serializer = self.get_serializer(hot_list_products, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["GET"],
        url_path="discounted",
        permission_classes=[AllowAny],
    )
    def discounted_list(self, request):
        discounted_list_products = self.get_queryset()
        serializer = self.get_serializer(discounted_list_products, many=True)
        return Response(serializer.data)


class ProductImageViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs["product_pk"])
