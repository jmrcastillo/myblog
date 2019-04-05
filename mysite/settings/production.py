

from .base import *

import django_heroku

DEBUG = True

# security warning: keep the secret key used in production secret!
SECRET_KEY = 'n6$gz-vsdfadf84=@((@%%s*ak@wp!c)bxk$w3)js-0fhogp0m(#xab$'

ALLOWED_HOSTS = ['myblog-jmr.herokuapp.com']

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

django_heroku.settings(locals())
