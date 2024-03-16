from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)

    email = None
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
