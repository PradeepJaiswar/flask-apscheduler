from celery import Celery
from config import get_config

app = Celery(get_config().CELERY_CRWALER_WORKER, broker=get_config().CELERY_BROKER_URL)

@app.task(name='flask-rest-api.tasks.crawl')
def crawl(message):
    for number in range(100):
        print(number)
