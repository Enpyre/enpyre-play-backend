from rest_framework.test import APIClient

from enpyre_play.projects.models import Project


class TestCreateProjectSolutionViewset:
    def test_create_project_solution(self, user, authenticated_client: APIClient):
        project = Project.objects.get(user=user)
        response = authenticated_client.post(
            f'/projects/{project.id}/solutions/mine',
            data={'code': 'print("Hello, World!")', 'project': project.id},
            format='json',
        )

        print(response.data)
        assert response.status_code == 201
        response_json: dict = response.json()
        assert response_json.pop('id') is not None
        assert response_json.pop('updated_at') is not None
        assert response_json.pop('created_at') is not None
        assert response_json == {
            'project': project.id,
            'code': 'print("Hello, World!")',
            'user': user.id,
        }
