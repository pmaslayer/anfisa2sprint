# ice_cream/apps.py
from django.apps import AppConfig

class IceCreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ice_cream'
    # Добавить строчку:
    verbose_name = 'Каталог мороженого'