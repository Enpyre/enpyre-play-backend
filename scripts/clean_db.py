from enpyre_play.projects.models import Project
from enpyre_play.users.models import User


class CleanDB:
    @classmethod
    def run(cls):
        Project.objects.all().delete()
        User.objects.all().delete()
