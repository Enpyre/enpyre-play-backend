from django.contrib.auth import get_user_model


class CleanDB:
    @classmethod
    def run(cls):
        get_user_model().objects.all().delete()
