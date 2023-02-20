from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enpyre_play.projects'

    def ready(self):
        from . import signals  # noqa
