from celery import Celery
import os
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atomic_habits.settings')

app = Celery('atomic_habits')
app.config_from_object('django.conf:settings')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()