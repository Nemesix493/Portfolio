import os

ENV = os.getenv('ENV')

if ENV:
    if ENV == 'PRODUCTION':
        from .production import *  # noqa: F403, F401
    elif ENV == 'PRODUCTION_TEST':
        from .production_test import *  # noqa: F403, F401
    elif ENV == 'DEV':
        from .dev import *  # noqa: F403, F401
else:
    from .dev import *  # noqa: F403, F401
