from enpyre_play.quizzes.enums import QuizzTypeSet
from enpyre_play.quizzes.models import Quizz


class PopulateQuizz:
    @classmethod
    def run(cls, user, **kwargs):
        quizz, _ = Quizz.objects.get_or_create(
            title=kwargs.get('title', 'Test Quizz'),
            defaults={
                'description': kwargs.get('description', 'Test Quizz Description'),
                'quizz_type': kwargs.get('quizz_type', QuizzTypeSet.MULTIPLE_CHOICE),
                'owner': user,
            },
        )
        return quizz
