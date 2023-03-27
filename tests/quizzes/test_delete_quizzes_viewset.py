import pytest
from rest_framework.test import APIClient

from enpyre_play.quizzes.models import Quizz, QuizzAnswer, QuizzQuestion


@pytest.mark.skip('Fix later.')
class TestDeleteQuizzesViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/quizzes/'

    def test_delete_quizz(self, authenticated_client: APIClient, db):
        quizz = Quizz.objects.only('id').first()
        assert quizz is not None
        quizz_id = quizz.id
        response = authenticated_client.delete(f'{self.url}{quizz_id}/')
        assert response.status_code == 204
        assert Quizz.objects.filter(id=quizz_id).count() == 0
        assert QuizzQuestion.objects.filter(quizz_id=quizz_id).count() == 0
        assert QuizzAnswer.objects.filter(question__quizz_id=quizz_id).count() == 0
