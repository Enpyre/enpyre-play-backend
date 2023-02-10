from .populate_project import PopulateProject
from .populate_quizz import PopulateQuizz
from .populate_quizz_answer import PopulateQuizzAnswer
from .populate_quizz_question import PopulateQuizzQuestion
from .populate_user import PopulateUser


class PopulateDB:
    @classmethod
    def run(cls):
        user = PopulateUser.run()
        user_shared_public = PopulateUser.run(suffix='shared-public')
        user_shared = PopulateUser.run(suffix='shared')
        user_public = PopulateUser.run(suffix='public')
        PopulateProject.run(
            user, shared=False, public=False, link_uuid='e3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
        )
        PopulateProject.run(
            user_shared_public,
            shared=True,
            public=True,
            link_uuid='ef772583-babd-4fd7-9729-15a3ed096719',
        )
        PopulateProject.run(
            user_shared, shared=True, public=False, link_uuid='c3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
        )
        PopulateProject.run(
            user_public, shared=False, public=True, link_uuid='d3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
        )
        quizz = PopulateQuizz.run(user)
        questions = [
            {
                'title': 'Test Quizz Question 1',
                'content': 'Test Quizz Question 1 Content',
                'position': 0,
            },
            {
                'title': 'Test Quizz Question 2',
                'content': 'Test Quizz Question 2 Content',
                'position': 1,
            },
            {
                'title': 'Test Quizz Question 3',
                'content': 'Test Quizz Question 3 Content',
                'position': 2,
            },
        ]
        answers = [
            [
                {
                    'title': 'Test Quizz Answer 1',
                    'content': 'Test Quizz Answer 1 Content',
                    'is_correct': True,
                    'score_amount': 1,
                    'position': 0,
                },
                {
                    'title': 'Test Quizz Answer 2',
                    'content': 'Test Quizz Answer 2 Content',
                    'is_correct': False,
                    'score_amount': 0,
                    'position': 1,
                },
                {
                    'title': 'Test Quizz Answer 3',
                    'content': 'Test Quizz Answer 3 Content',
                    'is_correct': False,
                    'score_amount': 0,
                    'position': 2,
                },
            ],
            [
                {
                    'title': 'Test Quizz Answer 4',
                    'content': 'Test Quizz Answer 4 Content',
                    'is_correct': False,
                    'score_amount': 0,
                    'position': 0,
                },
                {
                    'title': 'Test Quizz Answer 5',
                    'content': 'Test Quizz Answer 5 Content',
                    'is_correct': True,
                    'score_amount': 1,
                    'position': 1,
                },
                {
                    'title': 'Test Quizz Answer 6',
                    'content': 'Test Quizz Answer 6 Content',
                    'is_correct': False,
                    'score_amount': 0,
                    'position': 2,
                },
            ],
            [
                {
                    'title': 'Test Quizz Answer 7',
                    'content': 'Test Quizz Answer 7 Content',
                    'is_correct': False,
                    'score_amount': 0,
                    'position': 0,
                },
                {
                    'title': 'Test Quizz Answer 8',
                    'content': 'Test Quizz Answer 8 Content',
                    'is_correct': False,
                    'score_amount': 0,
                    'position': 1,
                },
                {
                    'title': 'Test Quizz Answer 9',
                    'content': 'Test Quizz Answer 9 Content',
                    'is_correct': True,
                    'score_amount': 1,
                    'position': 2,
                },
            ],
        ]
        for question, answer in zip(questions, answers):
            quizz_question = PopulateQuizzQuestion.run(quizz, **question)
            for answer_item in answer:
                PopulateQuizzAnswer.run(quizz_question, **answer_item)
