# from enpyre_play.enums import EnvironmentSet
from enpyre_play.enums import EnvironmentSet
from enpyre_play.envs import ENVIRONMENT, JWT_SECRET_KEY

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = JWT_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENVIRONMENT == EnvironmentSet.DEVELOPMENT
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://enpyre-play.vercel.app',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'https://enpyre-play.vercel.app',
]
