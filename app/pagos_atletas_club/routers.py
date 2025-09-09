from flask_restx import Resource
from .documentation import *



@api.route('/api/v1')
class  GestionPago(Resource):
    def get(self):
        return {"purbe":1}