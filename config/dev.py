from base import BaseConfig

class DevConfig(BaseConfig):

   # Statement for enabling the development environment
   DEBUG = True

   # Secret key for signing cookies
   SECRET_KEY = 'development key'

   #CELERY_BROKER_URL =  'amqp://guest@localhost//'
   CELERY_BROKER_URL =  'redis://localhost:6379/0'

   KAFAK_BOOSTRAP_SERVERS = 'localhost:9092'
