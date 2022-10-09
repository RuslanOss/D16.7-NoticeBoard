import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Billboard.settings')

app = Celery('Billboard')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every minute': {
        'task': 'NoticeBoard.tasks.delete_old_codes',
        'schedule': crontab(),
    }
}

app.autodiscover_tasks()