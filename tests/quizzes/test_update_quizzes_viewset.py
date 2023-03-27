import pytest
from rest_framework.test import APIClient

from enpyre_play.quizzes.models import Quizz


@pytest.mark.skip('Fix later.')
class TestUpdateQuizzesViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/quizzes/'

    def test_update_quizz(self, authenticated_client: APIClient, db):
        quizz = Quizz.objects.only('id').first()
        assert quizz is not None
        quizz_id = quizz.id
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
                    ],
                },
            ],
        }
        response = authenticated_client.put(f'{self.url}{quizz_id}/', data=data, format='json')
        assert response.status_code == 200
        response_json: dict = response.json()

        questions = response_json.pop('questions')
        questions_data = data.pop('questions')
        owner = response_json.pop('owner')

        assert owner.pop('id') is not None
        assert owner == {
            'first_name': 'Test',
            'last_name': 'User',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa: E501
        }

        assert response_json.pop('id') == quizz_id
        assert response_json == data

        questions_data.reverse()  # type: ignore
        for question_data, question in zip(questions_data, questions):
            answers = question.pop('answers')
            answers_data = question_data.pop('answers')  # type: ignore
            assert question.pop('id') is not None

            assert question_data == question

            answers_data.reverse()
            for answer_data, answer in zip(answers_data, answers):
                assert answer.pop('id') is not None
                assert answer_data == answer
