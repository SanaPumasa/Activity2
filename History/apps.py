from django.apps import AppConfig

class History(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'History'

    def ready(self):
        import History.signals
