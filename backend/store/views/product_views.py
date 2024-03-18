from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from ..models import Product, ProductImage
from ..serializers import (
    ProductSerializer,
    ProductImageSerializer,
    SimpleProductSerializer,
)


class ProductViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = SimpleProductSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductSerializer
        return SimpleProductSerializer


class ProductImageViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs["product_pk"])
