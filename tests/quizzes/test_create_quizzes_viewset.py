import pytest
from rest_framework.test import APIClient

from enpyre_play.quizzes.models import Quizz, QuizzAnswer, QuizzQuestion


class TestCreateQuizzesViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/quizzes/'

    def test_create_quizz(self, authenticated_client: APIClient, db):
        data = {
            'title': 'Test Quizz',
            'description': 'Test Quizz Description',
            'quizz_type': 'multiple_choice',
            'questions': [
                {
                    'title': 'Test Quizz Question 1',
                    'content': 'Test Quizz Question 1 Content',
                    'position': 0,
                    'answers': [
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
                },
                {
                    'title': 'Test Quizz Question 2',
                    'content': 'Test Quizz Question 2 Content',
                    'position': 1,
                    'answers': [
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
                },
                {
                    'title': 'Test Quizz Question 3',
                    'content': 'Test Quizz Question 3 Content',
                    'position': 2,
                    'answers': [
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
                },
            ],
        }

        response = authenticated_client.post(self.url, data=data, format='json')

        assert response.status_code == 201
        response_json: dict = response.json()

        quizz_id = response_json.pop('id')
        assert quizz_id is not None

        owner = response_json.pop('owner')
        assert owner.pop('id') is not None
        assert owner == {
            'email': 'test@enpyre.com.br',
            'first_name': 'Test',
            'last_name': 'User',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa: E501
        }

        questions_data = data.pop('questions')
        questions = response_json.pop('questions')
        assert len(questions) == len(questions_data)
        assert response_json == data

        questions_data.reverse()  # type: ignore
        for question_data, question in zip(questions_data, questions):
            assert question.pop('id') is not None
            answers_data = question_data.pop('answers')  # type: ignore
            answers = question.pop('answers')
            assert len(answers) == len(answers_data)
            assert question == question_data
            answers_data.reverse()
            for answer_data, answer in zip(answers_data, answers):
                assert answer.pop('id') is not None
                assert answer == answer_data

        assert Quizz.objects.filter(id=quizz_id).count() == 1
        assert QuizzQuestion.objects.filter(quizz_id=quizz_id).count() == 3
        assert QuizzAnswer.objects.filter(question__quizz_id=quizz_id).count() == 9
