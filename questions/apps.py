from django.apps import AppConfig


class UserAnswerConfig(AppConfig):
    name = "questions"
    verbose_name = 'User Answers'

    def ready(self):
        from . import signals
