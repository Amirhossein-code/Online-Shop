from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    PermissionsMixin,
)
from django.core.validators import validate_email
from django.db import models


class UserManager(BaseUserManager):
    """
    User Manager.
    To create superuser.
    """

    def create_user(self, email, password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model.
    """

    email = models.EmailField(
        max_length=50, blank=True, null=True, validators=[validate_email], unique=True
    )

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_registered_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email
