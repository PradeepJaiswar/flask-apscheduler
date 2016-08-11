import os

from flask_restful import reqparse, Resource
from app.api import api

import crawl_worker
from random import randint

#get url from post
parser = reqparse.RequestParser()
parser.add_argument('url')

class UrlsResource(Resource):

    def post(self):
        args = parser.parse_args()
        #add celery job here
        crawl_worker.crawl.delay()
        #for now make dummy response with post url parameters
        response = {
           'job_id' : randint(0,1000),
           'status' : "queued",
           'description' : 'Your crawling reuest for url  is accpeted',
           'env' : os.environ.get('APP_ENV'),

        }
        return response,200

api.add_resource(UrlsResource, '/urls')
