from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
)
from ..models import ProductReview
from ..serializers import ProductReviewSerializer
from ..paginations import NormalPagination


class ProductReviewViewSet(ModelViewSet):
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = NormalPagination

    def get_serializer_context(self):
        return {"product_slug": self.kwargs["product_slug"]}

    def get_queryset(self):
        return ProductReview.objects.filter(
            product__slug=self.kwargs["product_slug"], status=ProductReview.APPROVED
        )

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)
