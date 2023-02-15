from decouple import config

from .enums import EnvironmentSet

ENVIRONMENT = config('ENVIRONMENT', default=EnvironmentSet.DEVELOPMENT, cast=EnvironmentSet)
PYTEST_RUNNING = config('PYTEST_RUNNING', default=False, cast=bool)

GITHUB_KEY = config('GITHUB_KEY', default=None)
GITHUB_SECRET = config('GITHUB_SECRET', default=None)

DB_NAME = config('DB_NAME', default='enpyre_db')
DB_USER = config('DB_USER', default='enpyre')
DB_PASSWORD = config('DB_PASSWORD', default='enpyre')
DB_HOST = config('DB_HOST', default='enpyre_postgres')
DB_PORT = config('DB_PORT', default=5432, cast=int)

JWT_SECRET_KEY = config('JWT_SECRET_KEY', default=None)

PROJECT_LINK_BASE_URL = config('PROJECT_LINK_BASE_URL', default='https://localhost:3000/projects/')
SENTRY_DSN = config('SENTRY_DSN', default=None)

RABBITMQ_DEFAULT_QUEUE = config('CELERY_DEFAULT_QUEUE', default='default')
RABBITMQ_BROKER_URL = config(
    'CELERY_BROKER_URL', default='amqp://enpyre:enpyre@enpyre_rabbitmq:5672//'
)
