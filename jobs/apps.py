from django.apps import AppConfig


class JobConfig(AppConfig):
    name = "jobs"
    verbose_name = 'Jobs'

    def ready(self):
        from . import signals
