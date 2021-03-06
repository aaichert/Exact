"""
Django settings for exact project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", default='DEV KEY PLEASE CHANGE IN PRODUCTION INTO SOMETHING RANDOM')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default='127.0.0.1').split(" ")


# Application definition

INSTALLED_APPS = [
    'exact.annotations',
    'exact.base',
    'exact.images',
    'exact.users',
    'exact.tools',
    'exact.administration',
    'django.contrib.admin',
    'exact.tagger_messages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'widget_tweaks',
    'friendlytagloader',
    'plugins',
    'util',
    'django_registration'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'exact.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'exact.base.context_processors.base_data',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'exact.wsgi.application'

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


DATABASES = {
    'default': {
        # exact relies on some Postgres features so other Databses will _not_ work
        'ENGINE': os.environ.get("SQL_ENGINE", default='django.db.backends.postgresql_psycopg2'), #, default='django.db.backends.postgresql_psycopg2'
        'HOST': os.environ.get("SQL_HOST", default='127.0.0.1'), #, default='127.0.0.1'
        'NAME': os.environ.get("SQL_DATABASE", default='exact'), #, default='exact'
        'PASSWORD': os.environ.get("SQL_PASSWORD", default='exact'), #, default='exact'
        'USER': os.environ.get("SQL_USER", default='exact'), # , default='exact'
        'PORT': os.environ.get("SQL_PORT", default='5432'), #, default='5432'
    }
}

UPLOAD_FS_GROUP = os.environ.get("UPLOAD_FS_GROUP", 33)

AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'  # Timezone of your server

USE_I18N = True

USE_L10N = True

USE_TZ = False

PROBLEMS_URL = 'https://github.com/ChristianMarzahl/exact/issues'
PROBLEMS_TEXT = ''

LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/images/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.INFO: 'info',
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
    messages.SUCCESS: 'success',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

EXPORT_SEPARATOR = '|'
DATA_PATH = os.path.join(BASE_DIR, 'data')

IMAGE_PATH = os.path.join(BASE_DIR, 'images')  # the absolute path to the folder with the imagesets

MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL= "/media/"

# filename extension of accepted imagefiles
IMAGE_EXTENSION = {
    'png',
    'jpeg',
}

# Sets the default expire time for new messages in days
DEFAULT_EXPIRE_TIME = 7

# Sets the default number of messages per page
MESSAGES_PER_PAGE = 10
