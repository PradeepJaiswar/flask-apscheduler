import os

class BaseConfig(object):

   PROJECT_NAME = "app"

   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

   KAFKA_AUTO_OFFSET_REST = 'earliest'

   #logging setting
   LOGGING_FORMAT   = '%(asctime)s %(levelname)-8s %(correlationId)s %(message)s'

   LOGGING_LOCATION =  'logs/application.log'

   LOGGING_LEVEL = 'DEBUG'
