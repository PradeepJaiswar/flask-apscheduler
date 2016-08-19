import os

class BaseConfig(object):

   PROJECT_NAME = "app"

   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

   #logging setting
   LOGGING_FORMAT   = '%(asctime)s %(levelname)-8s %(correlationId)s %(message)s'
   LOGGING_LOCATION =  'logs/application.log'
   LOGGING_LEVEL = 'DEBUG'

   #API name settings
   API_URL_PREFIX = '/v1/api'
   API_VERSION = '0.1'
   BLUEPRINT_NAME = 'API v2'

   #swagger settings
   SWAGGER_HOST = 'localhost:5000'
   SWAGGER_DESCRIPTION = 'This is the version 1 of API'
   SWAGGER_API_SPEC_URL = '/docs/spec'
   SWAGGER_PRODUCES = ["application/json"]
