from .common import *
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = "django-insecure-)hf=%kwj)utr&6!*k)#kq^o5by0=8i45#r7%u!o53)dcldx7a_"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT"),
    }
}

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(" ")
