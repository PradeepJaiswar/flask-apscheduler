import os

class BaseConfig(object):

   PROJECT_NAME = "app"

   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

   DEBUG = False
   TESTING = False

   ADMINS = ['pradeep@jaiswar.in']

   # http://flask.pocoo.org/docs/quickstart/#sessions
   SECRET_KEY = 'secret key'

   KAFKA_AUTO_OFFSET_REST = 'earliest'
