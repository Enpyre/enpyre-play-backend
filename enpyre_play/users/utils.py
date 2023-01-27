from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(
        username='deleted',
        defaults={
            'email': 'deleted@enpyre.com.br',
            'first_name': 'Deleted',
            'last_name': 'User',
            'picture': (
                'https://api.dicebear.com/5.x/bottts-neutral/svg?'
                + 'seed=deleted&size=100&backgroundType=gradientLinear,solid'
            ),
        },
    )[0]
