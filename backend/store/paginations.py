from rest_framework.pagination import PageNumberPagination


class NormalPagination(PageNumberPagination):
    page_size = 50
