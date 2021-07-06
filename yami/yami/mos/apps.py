from django.apps import AppConfig


class MosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mos'
    verbose_name = 'Mos'
    list_display = ('key', 'full_name')
