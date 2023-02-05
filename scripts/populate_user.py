from enpyre_play.users.models import User


class PopulateUser:
    @classmethod
    def run(cls, suffix: str = ''):
        _suffix = f'-{suffix}' if suffix else ''
        user, _ = User.objects.get_or_create(
            email=f'test{_suffix}@enpyre.com.br',
            defaults=dict(
                username=f'test{_suffix}',
                first_name=f'Test{_suffix}',
                last_name=f'User{_suffix}',
                picture=(
                    'https://api.dicebear.com/5.x/bottts-neutral/svg?'
                    + f'seed=test{_suffix}&size=100&backgroundType=gradientLinear,solid'
                ),
            ),
        )
        return user
