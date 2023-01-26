from datetime import timedelta

from enpyre_play.envs import GITHUB_KEY, GITHUB_SECRET

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

ACTIVATE_JWT = True

SOCIAL_AUTH_PIPELINE = (
    'enpyre_play.users.social_pipeline.auto_logout',
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'enpyre_play.users.social_pipeline.check_for_email',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'enpyre_play.users.social_pipeline.save_avatar',
)

SOCIAL_AUTH_GITHUB_KEY = GITHUB_KEY
SOCIAL_AUTH_GITHUB_SECRET = GITHUB_SECRET
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email', 'read:user']

REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI = 'http://localhost:3000/login/callback/'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # 'ROTATE_REFRESH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True,
}

AUTH_USER_MODEL = 'users.User'
