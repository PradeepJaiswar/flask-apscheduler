import os

from logger import log
from flask_restful import reqparse, Resource
from app.api import api

from app.users import models


class LogsResource(Resource):

    def get(self):

        log().info('inside logs/get methog')
        log().warning('there is some problem in http hearder')
        log().debug('This is debuggin address')

        log().info('start making json response')
        response = {
           'job_id' : 100,
           'status' : "queued",
           'description' : 'Your crawling reuest for url  is accpeted',
        }

        log().info('done making json response')
        log().debug('response is '+ str(response))
        log().info('returning response')
        log().error('this is sample error msg')
        log().critical('this is sample critical msg')
        return response,200

api.add_resource(LogsResource, '/logs')
