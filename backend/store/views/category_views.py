from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from ..models import Category
from ..serializers import CategorySerializer
from ..filters import CategoryFilter
from ..paginations import NormalPagination


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = NormalPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
