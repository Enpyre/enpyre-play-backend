# from enpyre_play.enums import EnvironmentSet
from enpyre_play.envs import JWT_SECRET_KEY  # , ENVIRONMENT

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = JWT_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # ENVIRONMENT == EnvironmentSet.DEVELOPMENT
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']

CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']
