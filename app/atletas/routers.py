from flask import Blueprint
from flask_restx import  Resource
from .documentation import * 
from . import register_atletas
from ..auth import auth_user

atleta_bp = Blueprint('atleta', __name__, url_prefix='/atletas')



@api.route('/v1/api')
class Auth(Resource):
    @api.expect(payload_register, validate=True)
    @api.response(200, 'Atleta registrado exitosamente', respuesta_success)
    @api.response(400, 'Error de validación', respuesta_error)
    @api.response(500, 'Error interno del servidor', respuesta_error)
    def post(self):
        """Registro de atletas en el sistema"""
        try:        
            data = api.payload
            
            nombres=data["nombres"]
            apellidos=data["apellidos"]
            cedula=data["cedula"]
            fecha_nacimiento=data["fecha_nacimiento"]
            direccion=data["direccion"]
            telefono=data["telefono"]
            email=data["email"]
            username = data['username']
            password  = data['password']
            users_atleta  = auth_user.user_create(username, email, password)
            if users_atleta:
                register_atletas.register_atleta(users_atleta,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email)
                return {"Success":"Atleta Registrado exitosamente"}
            else:
                return {"Error":"Atleta no Registrado"}
        except ValueError as e:
            return {'Error':str(e)} , 400
        except Exception as e:
            return {'Error':str(e)} , 500