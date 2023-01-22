import hashlib

from rest_framework.response import Response


def auto_logout(*args, **kwargs):
    """Do not compare current user with new one"""
    return {'user': None}


def save_avatar(strategy, details, *args, user=None, **kwargs):
    """Get user avatar from social provider."""
    if user:
        backend_name = kwargs['backend'].__class__.__name__.lower()
        response = kwargs.get('response', {})
        picture = None
        if 'googleoauth2' in backend_name and response.get('image', {}).get('url'):
            picture = response['image']['url'].split('?')[0]
        elif 'github' in backend_name and response.get('avatar_url'):
            picture = response['avatar_url']
        else:
            picture = 'http://www.gravatar.com/avatar/'
            picture += hashlib.md5(user.email.lower().encode('utf8')).hexdigest()
            picture += '?size=100'
        if picture and user.picture != picture:
            user.picture = picture
            strategy.storage.user.changed(user)


def check_for_email(backend, uid, *args, user=None, **kwargs):
    if not kwargs['details'].get('email'):
        return Response({'error': "Email wasn't provided by oauth provider"}, status=400)
