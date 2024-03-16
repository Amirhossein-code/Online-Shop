from .common import *
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = "django-insecure-5io87@c17gn5$3=n1q*u2m#$+n*yzot5ca^!*()smv-nhwhvow"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
    }
}

CORS_ALLOWED_ORIGINS = []

ALLOWED_HOSTS = []
