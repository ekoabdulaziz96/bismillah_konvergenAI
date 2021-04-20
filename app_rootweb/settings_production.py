from .settings import *
import dj_database_url

import environ
env = environ.Env()

ALLOWED_HOSTS += ['bismillah-konvergen-ai.herokuapp.com']

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DJANGO_DEBUG', default=False, cast=bool)

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'