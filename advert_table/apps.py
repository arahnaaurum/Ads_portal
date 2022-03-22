from django.apps import AppConfig


class AdvertTableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advert_table'

    def ready(self):
        import advert_table.signals