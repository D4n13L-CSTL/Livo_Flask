from .documentation import *
from flask import request
from flask_restx import Resource
from . import services_entrenador
from flask_jwt_extended import  jwt_required




@api.route('')
class ClaseRouterEntrenador(Resource):
    
    @jwt_required()
    def post(self):
        try:
            data = api.payload
            username = data['username'].upper()
            email = data['email']
            password  = data['password']
            tipo_de_user = data.get('tipo_de_user_id')
            id_rol_club = data.get('id_rol_club')
            id_club = request.cookies.get('id_club_cookie')
            registro = services_entrenador.register_entrenador(username, email, password, tipo_de_user,id_club,id_rol_club)
            return {"Respuesta":"Entrenador Registrado correctamente"} , 200
        except Exception as e:
            return {'Error':str(e)} , 500