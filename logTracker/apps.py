from django.apps import AppConfig


class LogtrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logTracker'

    def ready(self):
        import logTracker.signals
