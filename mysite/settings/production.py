

from .base import *
import os


import django_heroku

DEBUG = False

# security warning: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['myblog-jmr.herokuapp.com']

DATABASES = {
    'default': {
    'engine': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'blog',
    'USER': 'postgres',
    'PASSWORD': 'ichoose',
    'HOST': '127.0.0.1',
    'PORT': '5432'
    }
}

django_heroku.settings(locals())
