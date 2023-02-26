from datetime import datetime

import pytest
from rest_framework.test import APIClient

from enpyre_play.projects.models import Project


class TestRetrieveProjectViewset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/projects/'

    def test_retrieve_project(self, db, user, authenticated_client: APIClient):
        project = Project.objects.get(user=user)
        response = authenticated_client.get(f'{self.url}{project.id}/')

        assert response.status_code == 200
        response_json: dict = response.json()

        assert datetime.fromisoformat(response_json.pop('created_at')) == project.created_at
        assert datetime.fromisoformat(response_json.pop('updated_at')) == project.updated_at
        assert response_json == {
            'id': project.id,
            'title': 'Test Project not shared not public',
            'description': 'This is a test project. It is not shared and not public.',
            'code': 'print("Hello, World!")',
            'link': 'https://localhost:3000/projects/e3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f/',
            'shared': False,
            'public': False,
            'user': {
                'id': user.id,
                'first_name': 'Test',
                'last_name': 'User',
                'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa: E501
            },
        }
