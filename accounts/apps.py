from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'Accounts'

    def ready(self):
        import .signals
