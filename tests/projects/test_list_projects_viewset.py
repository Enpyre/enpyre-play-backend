import pytest
from rest_framework.test import APIClient

from enpyre_play.envs import PROJECT_LINK_BASE_URL

SHARED_PUBLIC_PROJECT_LINK_ID = 'ef772583-babd-4fd7-9729-15a3ed096719'
SHARED_NOT_PUBLIC_PROJECT_LINK_ID = 'c3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
NOT_SHARED_PUBLIC_PROJECT_LINK_ID = 'd3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
NOT_SHARED_NOT_PUBLIC_PROJECT_LINK_ID = 'e3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'


class TestListProjectsViewset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/projects/'

    def test_get_all_public_projects(self, client_user_shared_public: APIClient):
        response = client_user_shared_public.get(self.url)

        assert response.status_code == 200
        response_json: dict = response.json()
        results = response_json.pop('results', [])
        assert response_json == {
            'count': 2,
            'next': None,
            'previous': None,
        }
        assert len(results) == 2

        self.assert_project_not_shared_public(results[0])

        self.assert_project_shared_public(results[1])

    def test_get_private_project(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.url)

        assert response.status_code == 200
        response_json: dict = response.json()
        results = response_json.pop('results', [])
        assert response_json == {
            'count': 3,
            'next': None,
            'previous': None,
        }
        assert len(results) == 3

        self.assert_project_not_shared_public(results[0])

        self.assert_project_shared_public(results[1])

        self.assert_project_not_shared_not_public(results[2])

    def test_get_only_shared_project(self, authenticated_client: APIClient):
        response = authenticated_client.get(
            f'{self.url}?link={PROJECT_LINK_BASE_URL + SHARED_NOT_PUBLIC_PROJECT_LINK_ID}'
        )

        assert response.status_code == 200
        response_json: dict = response.json()
        results = response_json.pop('results', [])
        assert response_json == {
            'count': 1,
            'next': None,
            'previous': None,
        }
        assert len(results) == 1

        self.assert_project_shared_not_public(results[0])

    def assert_project_shared_public(self, result: dict):
        assert result.pop('id') is not None
        user = result.pop('user')
        assert result.pop('updated_at') is not None
        assert result.pop('created_at') is not None
        assert result == {
            'title': 'Test Project shared public',
            'description': 'This is a test project. It is shared and public.',
            'code': 'print("Hello, World!")',
            'link': 'https://localhost:3000/projects/ef772583-babd-4fd7-9729-15a3ed096719/',
            'shared': True,
            'public': True,
        }
        assert user.pop('id') is not None
        assert user == {
            'email': 'test-shared-public@enpyre.com.br',
            'first_name': 'Test-shared-public',
            'last_name': 'User-shared-public',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test-shared-public&size=100&backgroundType=gradientLinear,solid',  # noqa
        }

    def assert_project_not_shared_public(self, result: dict):
        assert result.pop('id') is not None
        user = result.pop('user')
        assert result.pop('updated_at') is not None
        assert result.pop('created_at') is not None
        assert result == {
            'title': 'Test Project not shared public',
            'description': 'This is a test project. It is not shared and public.',
            'code': 'print("Hello, World!")',
            'link': 'https://localhost:3000/projects/d3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f/',
            'shared': False,
            'public': True,
        }
        assert user.pop('id') is not None
        assert user == {
            'email': 'test-public@enpyre.com.br',
            'first_name': 'Test-public',
            'last_name': 'User-public',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test-public&size=100&backgroundType=gradientLinear,solid',  # noqa
        }

    def assert_project_shared_not_public(self, result: dict):
        assert result.pop('id') is not None
        user = result.pop('user')
        assert result.pop('updated_at') is not None
        assert result.pop('created_at') is not None
        assert result == {
            'title': 'Test Project shared not public',
            'description': 'This is a test project. It is shared and not public.',
            'code': 'print("Hello, World!")',
            'link': 'https://localhost:3000/projects/c3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f/',
            'shared': True,
            'public': False,
        }
        assert user.pop('id') is not None
        assert user == {
            'email': 'test-shared@enpyre.com.br',
            'first_name': 'Test-shared',
            'last_name': 'User-shared',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test-shared&size=100&backgroundType=gradientLinear,solid',  # noqa
        }

    def assert_project_not_shared_not_public(self, result: dict):
        assert result.pop('id') is not None
        user = result.pop('user')
        assert result.pop('updated_at') is not None
        assert result.pop('created_at') is not None
        assert result == {
            'title': 'Test Project not shared not public',
            'description': 'This is a test project. It is not shared and not public.',
            'code': 'print("Hello, World!")',
            'link': 'https://localhost:3000/projects/e3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f/',
            'shared': False,
            'public': False,
        }
        assert user.pop('id') is not None
        assert user == {
            'email': 'test@enpyre.com.br',
            'first_name': 'Test',
            'last_name': 'User',
            'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa
        }
