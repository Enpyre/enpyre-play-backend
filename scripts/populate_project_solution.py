from enpyre_play.projects.models import ProjectSolution


class PopulateProjectSolution:
    @classmethod
    def run(cls, user, project):
        project_solution = ProjectSolution.objects.create(
            project=project,
            code='print("Hello, World!")',
            user=user,
        )
        return project_solution
