from django.apps import AppConfig


class SpyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.spy"

    def ready(self):
        import apps.spy.signals
