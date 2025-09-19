from .documentation import *
from flask_restx import Resource


@api.route('')
class AsistenciasClass(Resource):
    
    def get(self):
        
        return {'PRUEBA':"asdad"}
    
