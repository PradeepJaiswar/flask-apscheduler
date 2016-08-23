import os
from app.api import api
from logger import log
from pytz import utc
from datetime import datetime
import time

from flask import request, jsonify , json
from flask_restful import reqparse, Resource
from flask_restful_swagger_2 import swagger
from kafka import KafkaProducer


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore


####################################hack for apscheduler deafult handler##########################
import logging
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
####################################hack for apscheduler deafult handler##########################

####################################global scheduler init###################################
job_stores = {
    'default': RedisJobStore(jobs_key='apscheduler.jobs', run_times_key='apscheduler.run_times')
}
scheduler = BackgroundScheduler(jobstores=job_stores, timezone=utc)
scheduler.start()
###################################global scheduler init######################################

############################## global kafka publisher funnction ##############################
def publish_on_kafka(arg):
        from kafka import KafkaProducer
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('craw-url', b"test")
        producer.send('craw-url', b"\xc2Hola, mundo!")
############################## global kafka publisher funnction ##############################


class JobsResource(Resource):
    @swagger.doc({
        'tags': ['Jobs'],
        'summary': 'Reschedules a job',
        'description': "Reschedules job on specified run_time parameter",
        'parameters': [
            {
                'name': 'body',
                'default': '{"job_id":"87b8e099d7d147c993de0bf48df5de5a", "run_date": "2016-08-25 12:49:37"}',
                'description': 'Pass as raw body data',
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
                'description': 'Jobs',
                'schema': {},
                'examples': {
                    'application/json': {
                         	'data': {
                                "action": "start",
                                "args": "[{\"run_date\": \"2016-08-25 12:49:37\", \"url\": \"http://google.com\"}]",
                                "executor": "default",
                                "job_id": "87b8e099d7d147c993de0bf48df5de5a",
                                "job_name": "publish_on_kafka",
                                "next_run_time": "2016-08-25 12:49:37+00:00",
                                "run_date": "2016-08-25 12:49:37",
                                "url": "http://google.com"
                            }
                    }
                }
            }
        }
     })
    def put(self):
        #get post  parameters
        json_params  = json.loads(request.data)
        #check for url parameters
        if 'job_id' in json_params and json_params['job_id'] is not None and 'run_date' in json_params and json_params['run_date'] is not None:
            #get job id
            job_id =  json_params['job_id']
            #get job info
            job_obj = scheduler.get_job(str(job_id))
            #make sure job is there in job store
            if(job_obj is not None):
                #get new job time
                if('run_date' in json_params and json_params['run_date'] is not None):
                    job_time = json_params['run_date']
                else:
                    job_time = str(job_obj.next_run_time)

                ######################modify jobs############################
                job_obj_modify = scheduler.reschedule_job(job_obj.id, trigger='date', run_date=job_time)
                ######################modify jobs############################

                #make response from in modified job object
                response = {
                         "data": {
                             "job_id" : job_obj_modify.id,
                             "job_name" : job_obj_modify.name,
                             "run_date" : str(job_obj_modify.next_run_time),
                             "next_run_time" : str(job_obj_modify.next_run_time),
                             "executor" : job_obj_modify.executor,
                             "args" : json.dumps(job_obj_modify.args),
                         }
                  }
                return response ,200
            else:
                return {'error': 'no job found maching this job_id'}, 200
        else:
            return {'msg': 'Invalid parameters'} ,200
    @swagger.doc({
        'tags': ['Jobs'],
        'summary': 'Delete job',
        'description': "Removes job from job store",
        'parameters': [
            {
                'name': 'job_id',
                'description': 'job_id provided while creating job',
                'in': 'query',
                'required': 'true',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'Jobs',
                'schema': {},
                'examples': {
                    'application/json': {
                         	'data': {
                                 "args": "[{\"run_date\": \"2016-08-27 12:49:37\", \"url\": \"http://google.com\"}]",
                                 "executor": "default",
                                 "job_id": "562103739b294f298056e2d1eedd6ed9",
                                 "job_name": "publish_on_kafka",
                                 "next_run_time": "2016-08-27 12:49:37+00:00",
                                 "run_date": "2016-08-27 12:49:37+00:00"
                            }
                    }
                }
            }
        }
     })
    def delete(self):
         #get job_id from get
         job_id =request.args.get('job_id')

         if job_id is not None:
            #get job from job store
            job_obj = scheduler.get_job(str(job_id))
            if(job_obj is not None):
                #delete job from job store
                job_obj_del = scheduler.remove_job(str(job_id))
                #make response from previously fetch job
                response = {
                     "data": {
                         "job_id" : job_obj.id,
                         "job_name" : job_obj.name,
                         "next_run_time" : str(job_obj.next_run_time),
                         "executor" : job_obj.executor,
                         "args" : json.dumps(job_obj.args),
                         "status" : 'deleted',
                     }
                  }
                return response ,200
            else:
                return {'error': 'no job found maching this job_id'}, 200
         else:
            return {'error': 'job_id not found in parameters'}, 200

    @swagger.doc({
        'tags': ['Jobs'],
        'summary': 'Get job',
        'description': "Get information about already scheduled job",
        'parameters': [
            {
                'name': 'job_id',
                'description': 'job_id provided while creating job',
                'in': 'query',
                'required': 'true',
                'type': 'string',
            }
        ],
        'responses': {
            '200': {
                'description': 'Jobs',
                'schema': {},
                'examples': {
                    'application/json': {
                         	'data': {
                                 "args": "[{\"run_date\": \"2016-08-27 12:49:37\", \"url\": \"http://google.com\"}]",
                                 "executor": "default",
                                 "job_id": "562103739b294f298056e2d1eedd6ed9",
                                 "job_name": "publish_on_kafka",
                                 "next_run_time": "2016-08-27 12:49:37+00:00",
                                 "run_date": "2016-08-27 12:49:37+00:00"
                            }
                    }
                }
            }
        }
     })
    def get(self):
         #get job_id from get
         job_id =request.args.get('job_id')

         if job_id is not None:
             #get job from job store
             job_obj = scheduler.get_job(str(job_id))
             if(job_obj is not None):
                 #make response
                 response = {
                     "data": {
                         "job_id" : job_obj.id,
                         "job_name" : job_obj.name,
                         "run_date" : str(job_obj.next_run_time),
                         "next_run_time" : str(job_obj.next_run_time),
                         "executor" : job_obj.executor,
                         "args" : json.dumps(job_obj.args),
                     }
                 }
                 return response ,200
             else:
                  return {
                      'data': {
                          'error': 'no job found maching job_id'
                          }
                      },200
         else:
             return {
                 'data': {
                     'error': 'job_id not found'
                     }
                 },200

    @swagger.doc({
        'tags': ['Jobs'],
        'summary': 'Create new job',
        'description': "Create and schedules a new job specified in run_time parameters, if run_time is not provided job will be Schedules immediately using python datetime.now()",
        'parameters': [
            {
                'name': 'body',
                'default': '{"url":"http://google.com", "run_date": "2016-08-25 12:49:37"}',
                'description': 'Pass as raw body data',
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
                'description': 'Jobs',
                'schema': {},
                'examples': {
                    'application/json': {
                         	'data': {
                                "action": "start",
                                "args": "[{\"run_date\": \"2016-08-25 12:49:37\", \"url\": \"http://google.com\"}]",
                                "executor": "default",
                                "job_id": "87b8e099d7d147c993de0bf48df5de5a",
                                "job_name": "publish_on_kafka",
                                "next_run_time": "2016-08-25 12:49:37+00:00",
                                "run_date": "2016-08-25 12:49:37",
                                "url": "http://google.com"
                            }
                    }
                }
            }
        }
     })
    def post(self):
        #get post  parameters
        json_params  = json.loads(request.data)
        #check for url parameters
        if 'url' in json_params and json_params['url'] is not None:
                #check for date parameters
                if('run_date' in json_params and json_params['run_date'] is not None):
                    job_time = json_params['run_date']
                else:
                    job_time = str(datetime.now()) #set now if not define

                #################add-job#################
                job_obj = scheduler.add_job(publish_on_kafka, 'date', run_date=job_time, args=[json_params])
                #################add-job#################
                #make response
                response = {
                    "data": {
                        "job_id" : job_obj.id,
                        "job_name" : job_obj.name,
                        "run_date" : job_time,
                        "next_run_time" : str(job_obj.next_run_time),
                        "executor" : job_obj.executor,
                        "args" : json.dumps(job_obj.args),
                        "url" : json_params['url'],
                        "action" : 'start',
                    }
                }
                return response ,200
        else:
            return {
                'data': {
                    'error': 'invalid parameters'
                    }
                },200

api.add_resource(JobsResource, '/jobs')
