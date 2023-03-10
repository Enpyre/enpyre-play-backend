from enpyre_play.envs import PYTEST_RUNNING, RABBITMQ_BROKER_URL, RABBITMQ_DEFAULT_QUEUE

CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_TASK_DEFAULT_QUEUE = RABBITMQ_DEFAULT_QUEUE
CELERY_BROKER_URL = RABBITMQ_BROKER_URL
CELERY_MESSAGE_COMPRESSION = 'gzip'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_TASK_ALWAYS_EAGER = PYTEST_RUNNING
