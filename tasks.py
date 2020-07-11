from celery import Celery 
from time import sleep

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='db+sqlite:///db.sqlite3')

@app.task
def reverse(text):
    sleep(15)
    return text[::-1]
