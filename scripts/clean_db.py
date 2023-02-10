from enpyre_play.projects.models import Project
from enpyre_play.quizzes.models import Quizz, QuizzAnswer, QuizzQuestion
from enpyre_play.users.models import User


class CleanDB:
    @classmethod
    def run(cls):
        QuizzAnswer.objects.all().delete()
        QuizzQuestion.objects.all().delete()
        Quizz.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()
