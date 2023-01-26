from .populate_user import PopulateUser


class PopulateDB:
    @classmethod
    def run(cls):
        PopulateUser.run()
