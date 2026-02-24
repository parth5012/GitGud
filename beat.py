from celery import Celery
from dotenv import load_dotenv
import os


load_dotenv()

app =  Celery('my_app',broker=os.getenv('CELERY_BROKER_URL'))

app.conf.beat_schedule = {
    'find_issues': {
        'task': 'tasks.my_task',
        'schedule': 3000,
    },
}