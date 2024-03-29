from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import ProductReview
from ..serializers import ProductReviewSerializer, DisplayProductReviewSerializer
from ..permissions import IsObjectOwner
from ..filters import ProductReviewFilter
from ..paginations import NormalPagination


class MyProductReviewViewSet(ModelViewSet):
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated, IsObjectOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductReviewFilter
    pagination_class = NormalPagination

    def get_serializer_context(self):
        return {"product_slug": self.kwargs["product_slug"]}

    def get_queryset(self):
        return ProductReview.objects.filter(
            product__slug=self.kwargs["product_slug"],
            customer=self.request.user.customer,
        ).all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


class ProductReviewViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = DisplayProductReviewSerializer
    permission_classes = [AllowAny]
    pagination_class = NormalPagination

    def get_queryset(self):
        return ProductReview.objects.filter(
            product__slug=self.kwargs["product_slug"],
            status=ProductReview.APPROVED,
        ).all()
