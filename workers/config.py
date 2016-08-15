#this is celery worker config file
import os

class BaseConfig(object):

   CELERY_CRWALER_WORKER = 'crawler'

   CELERY_TASK_PREFIX = 'flask-rest-api.tasks'

class DevConfig(BaseConfig):

   CELERY_BROKER_URL =  'amqp://guest@localhost//'

class LocalConfig(DevConfig):
   # config for local development
   pass

class ProdConfig(DevConfig):
    # config for production environment
    pass

class StagingConfig(DevConfig):
    # config for staging environment
    pass

def get_config():
   SWITCH = {
      'LOCAL'     : LocalConfig,
      'DEV'       : DevConfig,
      'STAGING'   : StagingConfig,
      'PRODUCTION': ProdConfig
   }
   if os.environ.get('APP_ENV'):
      return SWITCH[os.environ.get('APP_ENV')]
   else:
      return SWITCH['DEV']
