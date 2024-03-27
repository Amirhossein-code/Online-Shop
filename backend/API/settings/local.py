from .common import *
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = "django-insecure-5io87@c17gn5$3=n1q*u2m#$+n*yzot5ca^!*()smv-nhwhvow"

DEBUG = True


DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = []
