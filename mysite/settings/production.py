

from .base import *


DEBUG = False

ALLOWED_HOSTS = ['myblog-jmr.heroku.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'postgres',
        'PASSWORD': 'ichoose',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}