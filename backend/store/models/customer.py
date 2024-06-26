from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, editable=True)
    image = models.ImageField(upload_to="store/profile", null=True, blank=True)

    joined_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
