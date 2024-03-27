from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import CustomUserManager


class User(AbstractUser):
    """
    The authentication backend is set to be Email and Password
    the username is not used for login nor signup it is just a display name
    so we do not have to display user email when they interact with the
    system (like creating reviews)
    """

    email = models.EmailField(max_length=100, unique=True)
    display_name = models.CharField(max_length=150, unique=True)

    # Moced to Customer model for performance reasons
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
