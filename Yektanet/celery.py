import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')
app = Celery('Yektanet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
CELERY_TIMEZONE = 'Asia/Tehran'

app.conf.beat_schedule = {
    'save hourly data': {
        'task': 'hourly_task',
        'schedule': 3600.0
    },
    'save daily data': {
        'task': 'daily_task',
        'schedule': 86400.0
    },
}

