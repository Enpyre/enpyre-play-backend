from enpyre_play.quizzes.models import QuizzAnswer


class PopulateQuizzAnswer:
    @classmethod
    def run(cls, quizz_question, **kwargs):
        quizz_answer, _ = QuizzAnswer.objects.get_or_create(
            title=kwargs.get('title', 'Test Quizz Answer'),
            defaults={
                'content': kwargs.get('content', 'Test Quizz Answer Content'),
                'is_correct': kwargs.get('is_correct', False),
                'score_amount': kwargs.get('score_amount', 1),
                'position': kwargs.get('position', 0),
                'question': quizz_question,
            },
        )
        return quizz_answer
