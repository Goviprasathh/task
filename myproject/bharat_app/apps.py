from django.apps import AppConfig


class BharatAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bharat_app'
    
    
    def ready(self):
        from bharat_app import signals
