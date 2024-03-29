from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from ..models import Discount
from ..serializers import DisocuntSerializer


class DiscountViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Discount.objects.filter(public=True).all()
    serializer_class = DisocuntSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"
