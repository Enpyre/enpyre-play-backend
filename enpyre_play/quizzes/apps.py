from django.apps import AppConfig


class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enpyre_play.quizzes'

    def ready(self):
        from . import signals  # noqa
