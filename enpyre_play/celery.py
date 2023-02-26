import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enpyre_play.settings')

app = Celery('enpyre_play')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
