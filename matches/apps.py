from django.apps import AppConfig


class MatchConfig(AppConfig):
    name = "matches"
    verbose_name = 'Matches'

    def ready(self):
        from . import signals
