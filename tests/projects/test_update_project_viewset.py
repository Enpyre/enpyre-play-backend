from datetime import datetime

import pytest
from rest_framework.test import APIClient

from enpyre_play.projects.models import Project


class TestUpdateProjectViewset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/projects/'

    def test_update_project(self, db, user, authenticated_client: APIClient):
        project = Project.objects.get(user=user)

        response = authenticated_client.put(
            f'{self.url}{project.id}/',
            data={
                'title': 'Test Update Project',
                'description': 'This is a test update project.',
                'code': 'print("Hello, World Updated!")',
                'public': True,
                'shared': True,
            },
            format='json',
        )

        assert response.status_code == 200
        response_json: dict = response.json()

        assert response_json.get('updated_at') is not None
        assert response_json.pop('updated_at') != project.updated_at
        assert datetime.fromisoformat(response_json.pop('created_at')) == project.created_at

        assert response_json == {
            'id': project.id,
            'title': 'Test Update Project',
            'description': 'This is a test update project.',
            'code': 'print("Hello, World Updated!")',
            'link': project.link,
            'shared': True,
            'public': True,
            'user': {
                'id': user.id,
                'first_name': 'Test',
                'last_name': 'User',
                'picture': 'https://api.dicebear.com/5.x/bottts-neutral/svg?seed=test&size=100&backgroundType=gradientLinear,solid',  # noqa: E501
            },
        }

        project.refresh_from_db()

        assert project.title == 'Test Update Project'
        assert project.description == 'This is a test update project.'
        assert project.code == 'print("Hello, World Updated!")'
        assert project.public is True
        assert project.shared is True
