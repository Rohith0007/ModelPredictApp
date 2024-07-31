import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = ['*']
# CSRF_TRUSTED_ORIGINS = ['*']
DEBUG = False
SECRET_KEY = '(L.WJ}r^EGt%Jh2_^WQHXr,(Cuxf0@'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # Adjust this to match your front-end URL
# ]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# CONNECTION_STR = {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django-webapp-database",
        "HOST": "django-webapp-server.postgres.database.azure.com",
        "USER": "lmhgigcncb",
        "PASSWORD": "$Ko3yh87wprWoh3s"
    }
}

STATIC_ROOT = BASE_DIR/'staticfiles'

