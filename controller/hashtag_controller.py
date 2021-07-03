from exception.exceptions import InvalidDataException
from flask_restful import Resource
from flask import request
from service import post_service

 
class HashtagResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self, value):        
        try:
            page = request.args.get('page') if request.args.get('page') else 1
            per_page = request.args.get('per_page') if request.args.get('per_page') else 10

            return post_service.get_with_tag(value, page, per_page), 200
        except InvalidDataException as e:
            return str(e), 401
