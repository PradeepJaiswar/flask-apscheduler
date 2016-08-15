from base import BaseConfig

class DevConfig(BaseConfig):

   # Statement for enabling the development environment
   DEBUG = True

   # Secret key for signing cookies
   SECRET_KEY = 'development key'

   KAFKA_CRAWL_TOPIC = 'craw-url'

   KAFAK_BOOSTRAP_SERVERS = 'localhost:9092'
