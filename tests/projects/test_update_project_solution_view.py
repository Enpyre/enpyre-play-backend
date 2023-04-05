from rest_framework.test import APIClient

from enpyre_play.projects.models import Project


class TestUpdateProjectSolutionView:
    def test_update_project_solution(self, user, authenticated_client: APIClient):
        project = Project.objects.get(user=user)
        solution = project.solutions.first()

        assert solution.code == 'print("Hello, World!")'

        response = authenticated_client.patch(
            f'/projects/{project.id}/solutions/mine',
            data={'code': 'x = 1 * 7', 'project': project.id},
            format='json',
        )

        assert response.status_code == 200
        solution.refresh_from_db()

        assert solution.code == 'x = 1 * 7'
