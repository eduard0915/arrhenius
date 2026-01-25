from django.apps import AppConfig


class ProtocolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.protocol'
    verbose_name = 'Protocolo'

    def ready(self):
        import core.protocol.signals
