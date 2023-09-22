import os
import time
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_practice.settings')

app = Celery('django_celery_practice')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="addition_task")
def add(num1, num2):
    time.sleep(10)
    return num1 + num2
    
# Method 2 to use celery beat or celery periodic tasks.

# schedule time using a default method
# app.conf.beat_schedule = {
#     "clear-cache-in-10-sec": {
#         "task": "app.tasks.clear_cache",
#         "schedule": 10,
#         "args": (1234,)
#     }

#     # Add more new task here if needed
# }

# schedule time using timedelta
# app.conf.beat_schedule = {
#     "clear-cache-in-10-sec": {
#         "task": "app.tasks.clear_cache",
#         "schedule": timedelta(seconds=10),
#         "args": (1234,)
#     }

#     # Add more new task here if needed
# }

# schedule celery task time using crontab
app.conf.beat_schedule = {
    "clear-cache-in-10-sec": {
        "task": "app.tasks.clear_cache",
        "schedule": crontab(minute='*/1'), # run after every minute
        "args": (1234,)
    }

    # Add more new task here if needed
}

