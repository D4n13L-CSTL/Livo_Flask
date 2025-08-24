from flask import Blueprint
from flask_restx import Resource
from .documentation import *
from . import  login_iniar


login_bp = Blueprint('login', __name__, url_prefix='/login')

@api.route('/v1/api')
class Login(Resource):
    @api.expect(payload_login)
    @api.response(200, description='Respuesta Succes', model=respuesta_success)
    @api.response(401, 'Contraseña incorrecta', respuesta_error)
    @api.response(404, 'Usuario no encontrado', respuesta_error)
    @api.response(500, 'Error interno', respuesta_error)
    def post(self):
            """Api para login"""
            try:
                data = api.payload
                username = data['username']
                password = data['password']
                if username and password:
                    return login_iniar.login_user_service(username, password)
                else:
                     return {"Error":"Falta datos a enviar"}
            except Exception as e:
                 return {"Error":str(e)} , 500