from .common import *

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
