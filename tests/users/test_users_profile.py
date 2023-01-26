import pytest


class TestUsersProfile:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.endpoint = '/users/profile/'

    def test_get_profile(self, authenticated_client):
        response = authenticated_client.get(self.endpoint)
        assert response.status_code == 200
        response_json: dict = response.json()
        assert response_json.pop('id', None) is not None
        assert response_json == dict(
            email='test@enpyre.com.br',
            first_name='Test',
            last_name='User',
            picture='http://www.gravatar.com/avatar/88292cf6edfe61129f8c570ffaf92825?size=100',
        )
