from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestCelery.settings')

app = Celery('Test')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Asia/Ho_Chi_Minh'
app.autodiscover_tasks(settings.INSTALLED_APPS)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'Test cronjob': {
        'task': 'mypolls.tasks.add',
        'schedule': 5,  # crontab(second=53),
    },
}
