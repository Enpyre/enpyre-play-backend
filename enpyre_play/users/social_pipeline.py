from rest_framework.response import Response


def auto_logout(*args, **kwargs):
    """Do not compare current user with new one"""
    return {'user': None}


def save_avatar(strategy, *args, user=None, **kwargs):
    """Get user avatar from social provider."""
    if user:
        picture = 'https://api.dicebear.com/5.x/bottts-neutral/svg?'
        picture += f'seed={user.username}'
        picture += '&size=100&backgroundType=gradientLinear,solid'
        if user.picture != picture:
            user.picture = picture
            strategy.storage.user.changed(user)


def check_for_email(backend, uid, *args, user=None, **kwargs):
    if not kwargs['details'].get('email'):
        return Response({'error': "Email wasn't provided by oauth provider"}, status=400)
