from .populate_project import PopulateProject
from .populate_user import PopulateUser


class PopulateDB:
    @classmethod
    def run(cls):
        user = PopulateUser.run()
        user_shared_public = PopulateUser.run(suffix='shared-public')
        user_shared = PopulateUser.run(suffix='shared')
        user_public = PopulateUser.run(suffix='public')
        PopulateProject.run(
            user, shared=False, public=False, link_uuid='e3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
        )
        PopulateProject.run(
            user_shared_public,
            shared=True,
            public=True,
            link_uuid='ef772583-babd-4fd7-9729-15a3ed096719',
        )
        PopulateProject.run(
            user_shared, shared=True, public=False, link_uuid='c3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
        )
        PopulateProject.run(
            user_public, shared=False, public=True, link_uuid='d3b2b2f1-3b1f-4b1f-8c1f-1b1f3b1f4b1f'
        )
