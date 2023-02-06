import pytest
from rest_framework.test import APIClient

from enpyre_play.projects.models import Project


class TestDeleteProjectViewset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/projects/'

    def test_delete_project(self, db, user, authenticated_client: APIClient):
        project = Project.objects.get(user=user)
        response = authenticated_client.delete(f'{self.url}{project.id}/')

        assert response.status_code == 204

        with pytest.raises(Project.DoesNotExist):
            Project.objects.get(user=user)
