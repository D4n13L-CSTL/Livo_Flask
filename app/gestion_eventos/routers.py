from flask import Blueprint, make_response, request
from flask_restx import Resource
from .documentation import * 

gestion_bp = Blueprint('gestion_evento', __name__, url_prefix='/eventos')

@api.route('/api/v1')
class GestionarEventos(Resource):
    
    def get(self):
        return {'Valor':"PRUEBA"}