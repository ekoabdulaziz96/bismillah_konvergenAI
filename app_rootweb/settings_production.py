from .settings import *
import dj_database_url

# import environ
# env = environ.Env()
import os

ALLOWED_HOSTS += ['bismillah-konvergen-ai.herokuapp.com']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG')

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

INSTALLED_APPS += [whitenoise.runserver_nostatic]
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'