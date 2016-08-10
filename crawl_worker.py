import os
import sys

from celery import Celery


print sys.argv

from app.constants import constants as COMMON_CONSTANTS
from config.env import get_config

app = Celery(COMMON_CONSTANTS.CELERY_CRWALER_WORKER, broker=get_config().CELERY_BROKER_URL)

@app.task(name='flask-rest-api.tasks.crawl')
def crawl():
    for number in range(100):
        print(number)
