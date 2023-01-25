from enpyre_play.enums import EnvironmentSet
from enpyre_play.envs import ENVIRONMENT, JWT_SECRET_KEY

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = JWT_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENVIRONMENT == EnvironmentSet.DEVELOPMENT
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') if not DEBUG else None
SECURE_SSL_REDIRECT = not DEBUG
