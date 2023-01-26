from django.contrib.auth import get_user_model


class PopulateUser:
    @classmethod
    def run(cls):
        user, _ = get_user_model().objects.get_or_create(
            email='test@enpyre.com.br',
            defaults=dict(
                username='test',
                first_name='Test',
                last_name='User',
                picture='http://www.gravatar.com/avatar/88292cf6edfe61129f8c570ffaf92825?size=100',
            ),
        )
        return user
