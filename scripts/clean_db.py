from django.contrib.auth import get_user_model

from enpyre_play.projects.models import Project


class CleanDB:
    @classmethod
    def run(cls):
        Project.objects.all().delete()
        get_user_model().objects.all().delete()
