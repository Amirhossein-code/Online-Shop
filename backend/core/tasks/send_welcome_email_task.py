from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email_task(email):
    subject = "Welcome To The best Ecommerce Platform Ever!!!"
    message = "We are Glad To have you join us. Happy Shopping!!!"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
