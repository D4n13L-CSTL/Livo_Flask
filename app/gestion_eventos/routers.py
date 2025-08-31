from flask import Blueprint, make_response, request, jsonify
from flask_restx import Resource
from .documentation import * 
from . import creacion_de_eventos, obtener_eventos

gestion_bp = Blueprint('gestion_evento', __name__, url_prefix='/eventos')

@api.route('/api/v1')
class GestionarEventos(Resource):
    
    def post(self):
        try:
            data = api.payload
            nombre = data['nombre'] 
            descripcion = data['descripcion'] 
            fecha = data['fecha'] 
            hora = data['hora'] 
            id_tipo = data['id_tipo']
            id_de_evento = creacion_de_eventos.servicio_de_creacion(nombre, descripcion, fecha, hora, id_tipo)
            creacion_de_eventos.servicio_relacion_evento_club(id_de_evento)

            return {'Success':"Evento Registrado Exitosamente"}
        except Exception as e:
            return {"Error":str(e)} , 500
        
    
    def get(self):
        evento = obtener_eventos.readEventos()
        return make_response(jsonify(evento))