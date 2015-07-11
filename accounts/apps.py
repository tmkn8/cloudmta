from django.apps import AppConfig
from django.utils.translation import ugettext as _

class MyAppConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('Konta')

    def ready(self):
        import .signals
