from flask_restx import fields, Namespace

api = Namespace('Clubes', description='Gestión de clubes', path='/club')

# Payload esperado para registrar un club
payload_club = api.model('RegistroClub', {
    "nombre_de_club": fields.String(required=True, description="Nombre del club"),
    "nombre_administrador": fields.String(required=True, description="Nombre del administrador"),
    "email_club": fields.String(required=True, description="Correo electrónico del club"),
    "telefono_club": fields.String(required=True, description="Teléfono del club"),
    "username": fields.String(required=True, description="Usuario administrador del club"),
    "password": fields.String(required=True, description="Contraseña del usuario administrador")
})

# Respuestas
respuesta_success = api.model('RespuestaRegistroClubSuccess', {
    "Succes": fields.String(description="Mensaje de éxito")
})

respuesta_error = api.model('RespuestaRegistroClubError', {
    "Error": fields.String(description="Mensaje de error")
})
