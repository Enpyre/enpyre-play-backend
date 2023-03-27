import pytest
from rest_framework.test import APIClient


@pytest.mark.skip('Fix later.')
class TestListQuizzesViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/quizzes/'

    def test_get_all_quizzes(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.url)

        assert response.status_code == 200
        response_json: dict = response.json()
        results = response_json.pop('results', [])
        assert response_json == {
            'count': 1,
            'next': None,
            'previous': None,
        }
        assert len(results) == 1

        quizz = results[0]
        assert quizz.pop('id') is not None
        owner = quizz.pop('owner')
        questions = quizz.pop('questions')
        assert quizz == {
            'title': 'Test Quizz',
            'description': 'Test Quizz Description',
            'quizz_type': 'multiple_choice',
        }

        assert owner.pop('id') is not None
        assert owner == {
            'first_name': 'Test',
            'last_name': 'User',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa
        }

        questions.reverse()
        for i, question in enumerate(questions):
            assert question.pop('id') is not None
            answers = question.pop('answers')
            assert question == {
                'title': f'Test Quizz Question {i+1}',
                'content': f'Test Quizz Question {i+1} Content',
                'position': i,
            }

            answers.reverse()
            for j, answer in enumerate(answers):
                assert answer.pop('id') is not None
                assert answer == {
                    'title': f'Test Quizz Answer {3*i+j+1}',
                    'content': f'Test Quizz Answer {3*i+j+1} Content',
                    'is_correct': j == i,
                    'score_amount': 1 if j == i else 0,
                    'position': j,
                }
