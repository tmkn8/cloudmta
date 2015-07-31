from .common import *

# Nie używaj MyBB jako backendu
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Ne używaj SMTP do wysyłania emaili
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DEBUG = True

# Żeby dodawało port do URL przy przekierowaniu przez nginx
USE_X_FORWARDED_HOST = True

# URL do forum
FORUM_LINK = 'http://forum.cloudmta.dev:8080'

# Link do tworzenia kont
FORUM_REGISTER_ACCOUNT_LINK = FORUM_LINK + '/member.php?action=register'
