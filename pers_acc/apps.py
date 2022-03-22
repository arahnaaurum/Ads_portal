from django.apps import AppConfig


class PersAccConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pers_acc'

    def ready(self):
        import pers_acc.signals