from django.apps import AppConfig


class BlacklistedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blacklisted'
