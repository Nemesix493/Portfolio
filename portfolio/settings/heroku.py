import os

import dj_database_url

from .base import *  # noqa: F401, F403


DEBUG = False

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': db_from_env
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']  # noqa: F405
