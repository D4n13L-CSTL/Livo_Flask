from .documentation import *
from flask_restx import Resource

@api.route('/')
class RouteMembershi(Resource):
    
    def get(self):
        
        return {'PRueba':'PReba'}