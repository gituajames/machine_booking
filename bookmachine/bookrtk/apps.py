from django.apps import AppConfig


class BookrtkConfig(AppConfig):
    name = 'bookrtk'


    def ready(self):
        import bookrtk.signals
