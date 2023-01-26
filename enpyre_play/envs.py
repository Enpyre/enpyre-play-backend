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
