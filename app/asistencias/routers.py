from .documentation import *
from flask_restx import Resource


@api.route('/prueba')
class AsistenciasClass(Resource):
    
    def get(self):
        
        return {'PRUEBA':"asdad"}
    
