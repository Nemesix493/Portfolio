import os

ENV = os.getenv('ENV')

if ENV:
    if ENV == 'PRODUCTION':
        from .production import *
    elif ENV == 'PRODUCTION_TEST':
        from .production_test import *
    elif ENV == 'DEV':
        from .dev import *
else:
    from .dev import *