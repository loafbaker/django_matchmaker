from django.apps import AppConfig


class UserJobConfig(AppConfig):
    name = "profiles"
    verbose_name = 'User Jobs'

    def ready(self):
        from . import signals
