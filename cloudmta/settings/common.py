import os
import json
from pathlib import Path
from .roleplay import *
from django.contrib.messages import constants as message_constants

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Zaimportuj plik z tajnymi ustawieniami
try:
    with Path(os.path.join(BASE_DIR, 'settings', 'secrets.json')).open() as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {}

SECRET_KEY = SECRETS.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECRETS.get('DB_NAME', 'cloudmta'),
        'USER': SECRETS.get('DB_USER', 'cloudmta'),
        'PASSWORD': SECRETS.get('DB_PASSWORD', 'secret'),
        'HOST': SECRETS.get('DB_HOST', 'localhost'),
        'PORT': SECRETS.get('DB_PORT', '3306'),
    }
}

# Application definition
INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Third-party apps

    # My apps
    'characters',
    'accounts',
    'items',
    'vehicles',
    'groups',
    'doors',
    'pages',
    'wiki',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cloudmta.urls'

AUTHENTICATION_BACKENDS = ('accounts.backends.MyBBMemberBackend',)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(BASE_DIR), 'front', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Django context procesoors
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                # My own context processors
                'cloudmta.context_processors.settings_context_processor',
                'characters.context_processors.characters',
            ],
        },
    },
]

WSGI_APPLICATION = 'cloudmta.wsgi.application'

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

AUTH_USER_MODEL = 'accounts.User'

MESSAGE_TAGS = {
    message_constants.DEBUG: 'secondary',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'alert'
}

EMAIL_SUBJECT_PREFIX = '[CloudMTA]'

DEFAULT_AVATAR = 'img/default-avatar.png'
