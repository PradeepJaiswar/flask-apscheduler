import os

from logger import log
from flask_restful import reqparse, Resource
from app.api import api
from flask_restful_swagger_2 import swagger

class LogsResource(Resource):
    @swagger.doc({
        'tags': ['Logs'],
        'description': 'This api is for logging demo. Once you hit this api end point, logs will be appeded to log/application.log',
        'parameters': [
            {
                'name': 'correlation_id',
                'default': 'swagger-ui',
                'description': 'Correlation ID',
                'in': 'query',
                'required': 'true',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'Logs',
                "schema": {},
                'examples': {
                    'application/json': {
                         'status' : "logged",
                         'description' : 'Demo logs are added to log/application.log'
                    }
                }
            }
        }
     })
    def get(self):
        log().info('inside logs/get methog')
        log().warning('there is some problem in http hearder')
        log().debug('This is debuggin address')
        log().info('start making json response')
        response = {
           'status' : "logged",
           'description' : 'this is rest api for logging demo only.Demo logs are added to log/application.log',
        }
        log().info('done making json response')
        log().debug('response is '+ str(response))
        log().info('returning response')
        log().error('this is sample error msg')
        log().critical('this is sample critical msg')
        return response,200

api.add_resource(LogsResource, '/logs')
