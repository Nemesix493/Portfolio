import os

import dj_database_url

from .base import *


DEBUG = False

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': db_from_env
}

try:
    from .local import *
except ImportError:
    pass