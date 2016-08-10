import os

from local import LocalConfig
from dev import DevConfig
from stage import StagingConfig
from prod import ProdConfig

def get_config():
   SWITCH = {
      'LOCAL'     : LocalConfig,
      'DEV'       : DevConfig,
      'STAGING'   : StagingConfig,
      'PRODUCTION': ProdConfig
   }
   #return SWITCH[os.environ.get('ENV')]
   return SWITCH['DEV']
