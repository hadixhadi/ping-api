import os
from celery import Celery
from celery.schedules import schedule
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.envs.develop_settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
CELERY_TIMEZONE = "Asia/Tehran"
BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_RESULT_BACKEND = 'django-db'
