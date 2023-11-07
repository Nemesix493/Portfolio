import os

import dj_database_url

from .base import *  # noqa: F401, F403


DEBUG = False

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://portfolio-nginx"]
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': db_from_env
}
