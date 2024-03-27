from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import User
from ..tasks import send_welcome_email_task


@receiver(post_save, sender=User)
def send_welcome_email_on_create(sender, instance, created, **kwargs):
    if created:
        pass
        # send_welcome_email_task.delay(instance.email)
