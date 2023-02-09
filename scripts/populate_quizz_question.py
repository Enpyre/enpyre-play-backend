from enpyre_play.quizzes.models import QuizzQuestion


class PopulateQuizzQuestion:
    @classmethod
    def run(cls, quizz, **kwargs):
        quizz_question, _ = QuizzQuestion.objects.get_or_create(
            title=kwargs.get('title', 'Test Quizz Question'),
            defaults={
                'content': kwargs.get('content', 'Test Quizz Question Content'),
                'position': kwargs.get('position', 0),
                'quizz': quizz,
            },
        )
        return quizz_question
