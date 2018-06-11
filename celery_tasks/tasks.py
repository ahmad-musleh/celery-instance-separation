from celery import Celery
from os import environ
import time


CELERY_BROKER_URL = environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')
app = Celery(
    'tasks', 
    broker=CELERY_BROKER_URL, 
    backend=CELERY_RESULT_BACKEND
    )

@app.task
def taskA():
    time.sleep(5)
    return "Task A is done!!"

@app.task
def taskB():
    time.sleep(10)
    return "Task B is done!!"