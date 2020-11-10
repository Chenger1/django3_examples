from .base import *


DEBUG = False


ADMIN = (
    ('nitron', 'admin@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'SOME_USER',
        'PASSWORD': '********'
    }
}
