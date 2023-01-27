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
                picture=(
                    'https://api.dicebear.com/5.x/bottts-neutral/svg?'
                    + 'seed=test&size=100&backgroundType=gradientLinear,solid'
                ),
            ),
        )
        return user
