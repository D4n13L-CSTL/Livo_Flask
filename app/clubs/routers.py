from flask import Blueprint
from flask_restx import Resource
from .documentation import * 
from . import gestion_club
from ..auth import auth_user

club_bp = Blueprint('club', __name__, url_prefix='/club')



@api.route('/v1/api')
class ClubRest(Resource):
    @api.expect(payload_club, validate=True)
    @api.response(200, 'Club registrado correctamente', respuesta_success)
    @api.response(400, 'Error en los datos enviados', respuesta_error)
    @api.response(500, 'Error interno del servidor', respuesta_error)
    def post(self):
        """Registro de un club con su usuario administrador"""
        try:
            data = api.payload

            nombre = data["nombre_de_club"]
            administrador = data["nombre_administrador"]
            email = data["email_club"]
            telefono = data["telefono_club"]
            username = data['username']
            password = data['password']

            club_register = gestion_club.register_club_id(nombre, administrador, email, telefono)
            if not club_register:
                return {"Error": "Club no registrado"}, 400

            club_user_register = auth_user.user_create(username, email, password)
            if not club_user_register:
                return {"Error": "Usuario del club no registrado"}, 400

            
            gestion_club.register_user_club_class(club_user_register, club_register, 1)

            return {"Succes": "Club registrado correctamente"}, 200
        except Exception as e:
            return {"Error": str(e)}, 500