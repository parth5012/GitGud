from celery import Celery
from dotenv import load_dotenv
import os


load_dotenv()

app =  Celery('my_app',broker=os.getenv('CELERY_BROKER_URL'))

app.autodiscover_tasks(['utils.tasks'])

app.conf.beat_schedule = {
    'find_issues': {
        'task': 'utils.tasks.send_issues_to_discord',
        'schedule': 3000,
    },
}