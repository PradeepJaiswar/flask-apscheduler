from flask import Blueprint
from flask_restful_swagger_2 import Api

from config.env import get_config

api_blueprint = Blueprint(get_config().BLUEPRINT_NAME, __name__, url_prefix=get_config().API_URL_PREFIX)
# api = Api(api_blueprint)

# This is important for swagger to put document right
api = Api(api_blueprint, api_version=get_config().API_VERSION,
                       base_path=get_config().API_URL_PREFIX,
                       host=get_config().SWAGGER_HOST,
                       produces=get_config().SWAGGER_PRODUCES,
                       api_spec_url=get_config().SWAGGER_API_SPEC_URL,
                       description=get_config().SWAGGER_DESCRIPTION)

# Import the resources to add the routes to the blueprint before the app is
# initialized
from . import logs  # NOQA
