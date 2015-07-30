from .common import *

# Nie używaj MyBB jako backendu
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

DEBUG = True

USE_X_FORWARDED_HOST = True

SECRET_KEY = 'ag-2q%m@db=9or8kc*==p9ssz36v38w@@as+-(ru8e&!27qrrj'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudmta',
        'USER': 'cloudmta',
        'PASSWORD': 'secret',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# URL do forum
FORUM_LINK = 'http://forum.cloudmta.dev:8080'
# Link do tworzenia kont
FORUM_REGISTER_ACCOUNT_LINK = FORUM_LINK + '/member.php?action=register'
