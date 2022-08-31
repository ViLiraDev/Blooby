from django.apps import AppConfig


class BloobyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blooby'

    def ready(self):
        import Blooby.signals