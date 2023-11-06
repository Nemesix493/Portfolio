import os

from .base import *  # noqa: F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-51-ck1kht4^88bzk3+987_jkdb95!j(w8ajf(ms#@dvd+=c8^9"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),  # noqa: F405
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
