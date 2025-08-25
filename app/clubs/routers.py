from flask import Blueprint, make_response, jsonify, request
from flask_restx import Resource
from .documentation import * 
from . import gestion_club, formularios_registrados, link_generate_inscripcion
from ..auth import auth_user
from flask_jwt_extended import decode_token

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
            formulario_data = data.get('formulario')  

            gestion_club.formulario_inscripcion(formulario_data)
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
        


@api.route('/v1/api/formulario/<int:id_formulario>/invitacion')
class GenerarLinkInscripcion(Resource):
    def post(self,id_formulario):
        try:
            id_club = request.cookies.get("id_club_cookie")
            print(id_club)
            link  = link_generate_inscripcion.generar_link(id_club, id_formulario)
            return {"Link":link}      
        except Exception as e:
            return {"Error":str(e)} , 500
        


@api.route('/v1/api/registro_atleta')
class obtener_formulario(Resource):
    def get(self):
        token = request.args.get("token")
        if not token:
            return {"error": "Falta token"}, 40

        try:
            # Decodificamos sin necesidad de que sea un usuario logueado
            data = decode_token(token)
            id_club = data["id_club"]
            id_formulario = data["id_formulario"]

            # Buscar el formulario
            formulario = formularios_registrados.formulario_for_id(id_club, id_formulario)
            if not formulario:
                return {"error": "Formulario no encontrado"}, 404

            return {"formulario": formulario, "id_club": id_club}, 200

        except Exception as e:
            return {"error": str(e)}, 400
        
    