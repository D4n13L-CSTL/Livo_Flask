from flask import Blueprint, make_response, jsonify
from flask_restx import Resource
from .documentation import * 
from . import gestion_club, formularios_registrados
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
    

@api.route('/v1/api/formulario')
class FormularioClub(Resource):
    @api.expect(payload_formulario)
    @api.response(200, 'Formulario creado correctamente', respuesta_formulario_success)
    @api.response(500, 'Error interno', respuesta_formulario_error)

    def post(self):
        """Crea un formulario de inscripción para un club.

        Recibe un JSON con:
        - `id_club`: ID del club.
        - `formulario`: diccionario dinámico con los campos y tipos de datos del formulario.
        """
        try:
            data = api.payload
            id_club = data.get('id_club')
            formulario_data = data.get('formulario')  

            gestion_club.formulario_inscripcion(formulario_data, id_club)
            return {"Response":"Formulario creado correctamente"} , 200
        
        except Exception as e:
            return {"Error":str(e)} , 500


@api.route('/v1/api/formulario/<id_club>')
class VerFormularioClub(Resource):
    @api.response(200, 'Formulario del club', payload_formulario)
    @api.response(500, 'Error interno', respuesta_formulario_error)
    def get(self,id_club):
        """Obtiene el formulario de inscripción de un club por su ID."""
        try:
            club_formulario = formularios_registrados.ver_formularios(id_club)
            return make_response(jsonify(club_formulario))
        except Exception as e:
            return {"Error":str(e)} , 500
        
