from flask import Blueprint, request
from flask_jwt_extended import decode_token
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
        token = request.args.get("token")
        data = request.json  # datos enviados por el atleta (payload dinámico + fijo)

        if not token:
            return {"error": "Falta token"}, 400

     
        # 1. Decodificar token
        claims = decode_token(token)
        id_club = claims["id_club"]

        id_formulario = claims["id_formulario"]

        # 2. Datos básicos del atleta (como en tu otro endpoint)
        nombres = data.get("nombres")
        apellidos = data.get("apellidos")
        cedula = data.get("cedula")
        fecha_nacimiento = data.get("fecha_nacimiento")
        direccion = data.get("direccion")
        telefono = data.get("telefono")
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        # 3. Crear usuario y atleta
        users_atleta = auth_user.user_create(username, email, password)
        if not users_atleta:
            return {"Error": "No se pudo crear el usuario"}, 400

        id_atleta = register_atletas.register_atleta(
            users_atleta, nombres, apellidos, cedula, fecha_nacimiento,
            direccion, telefono, email
        )
        # 4. Relacionar atleta con el club
        register_atletas.inscripcion_de_atleta(id_atleta, id_club)

        # 5. Guardar respuestas personalizadas del formulario
            #PARA GUARDAR LAS RESPUESTA DEL FORMULARIO EN OTRA TABLA 
        respuestas_formulario = data.get("respuestas", {})
        register_atletas.guardar_informacion_de_atleta(id_atleta, id_formulario,respuestas_formulario)
        return {
                "success": "Atleta registrado exitosamente",
                "id_atleta": id_atleta,
                "id_club": id_club
        }, 201

