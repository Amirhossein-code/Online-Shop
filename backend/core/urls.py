from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register("users", views.UserViewSet, basename="users")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path(
        "reset-password/",
        views.RequestPasswordResetView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password/<uuid:token>/",
        views.ResetPasswordView.as_view(),
        name="reset-password-confirm",
    ),
]

urlpatterns += router.urls
