from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response("User registered successfully", status=status.HTTP_201_CREATED)
