import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated.settings')

app = Celery('automated')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True

# Auto-discover tasks in installed apps
app.autodiscover_tasks()
