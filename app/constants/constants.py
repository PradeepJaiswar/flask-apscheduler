import os

# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

CELERY_CRWALER_WORKER = 'crawler'

CELERY_TASK_PREFIX = 'flask-rest-api.tasks'

KAFKA_CRAWL_TOPIC = 'craw-url'
