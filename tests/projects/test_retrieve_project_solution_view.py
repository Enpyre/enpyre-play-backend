from enpyre_play.projects.models import Project


class TestRetrieveProjectSolutionTestCase:
    def test_can_retrieve_solution(self, db, user, authenticated_client):
        project = Project.objects.get(user=user)
        project.solutions.first()
        url = f'/projects/{project.id}/solutions/mine'
        response = authenticated_client.get(url)

        assert response.status_code == 200

        data = response.data

        assert data['code'] == 'print("Hello, World!")'
        assert data['user'] == user.id
        assert data['project'] == project.id

    def test_cant_retrieve_solution_from_someone_else(
        self, db, user_shared_public, authenticated_client
    ):
        project = Project.objects.get(user=user_shared_public)
        project.solutions.first()
        url = f'/projects/{project.id}/solutions/mine'
        response = authenticated_client.get(url)

        assert response.status_code == 404
