from enpyre_play.projects.models import Project


class PopulateProject:
    @classmethod
    def run(cls, user, link_uuid: str, shared=False, public=False):
        shared_text = 'shared' if shared else 'not shared'
        public_text = 'public' if public else 'not public'
        project, _ = Project.objects.get_or_create(
            link=f'https://localhost:3000/projects/{link_uuid}/',
            defaults={
                'title': f'Test Project {shared_text} {public_text}',
                'description': f'This is a test project. It is {shared_text} and {public_text}.',
                'code': 'print("Hello, World!")',
                'public': public,
                'shared': shared,
                'user': user,
            },
        )
        return project
