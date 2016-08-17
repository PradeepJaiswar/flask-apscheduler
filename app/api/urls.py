import os

from flask import g
from flask_restful import reqparse, Resource
from flask_restful_swagger_2 import swagger

from app.api import api
from workers.crawl_worker import crawl
from random import randint

#get url from post
# parser = reqparse.RequestParser()
# parser.add_argument('url')

class UrlsResource(Resource):
    @swagger.doc({
        'tags': ['Urls'],
        'description': 'This is API will put the specificed url in parameters for scrapping',
        'parameters': [
            {
                'name': 'body',
                'default': "{'correlation_id' : 'swagger-ui'},{'url':'http://example.com'}",
                'description': 'Correlation ID',
                'in': 'body',
                'required': 'true',
                'type': 'json',
                'schema': {
                     "properties": {}
                  }
            }
        ],
        'responses': {
            '200': {
                'description': 'Urls',
                'schema': {},
                'examples': {
                    'application/json': {
                        'id': 1,
                        "description": "Your crawling reuest for url is accpeted and queued",
                        "job_id": 655,
                        "status": "queued"
                    }
                }
            }
        }
     })
    def post(self):
        #args = parser.parse_args()
        #add celery job here
        #crawl.delay(args.url)
        #for now make dummy response with post url parameters
        response = {
           'id'     : randint(0,1000),
           'job_id' : randint(0,1000),
           'status' : "queued",
           'description' : 'Your crawling reuest for url  is accpeted',
        }
        return response,200

api.add_resource(UrlsResource, '/urls')
