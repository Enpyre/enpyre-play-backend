import pytest
from rest_framework.test import APIClient


class TestCreateProjectViewset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/projects/'

    def test_create_project(self, authenticated_client: APIClient):
        response = authenticated_client.post(
            self.url,
            data={
                'title': 'Test Create Project',
                'description': 'This is a test project.',
                'code': 'print("Hello, World!")',
                'public': True,
            },
            format='json',
        )

        assert response.status_code == 201
        response_json: dict = response.json()
        user = response_json.pop('user')
        assert response_json.pop('id') is not None
        assert response_json.pop('link') is not None
        assert response_json.pop('updated_at') is not None
        assert response_json.pop('created_at') is not None
        assert response_json == {
            'title': 'Test Create Project',
            'description': 'This is a test project.',
            'code': 'print("Hello, World!")',
            'shared': False,
            'public': True,
        }
        assert user.pop('id') is not None
        assert user == {
            'first_name': 'Test',
            'last_name': 'User',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa: E501
        }
