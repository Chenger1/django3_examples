from .base import *


DEBUG = False


ADMIN = (
    ('nitron', 'admin@gmail.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'SOME_USER',
        'PASSWORD': '********'
    }
}
