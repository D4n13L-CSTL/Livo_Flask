from flask_restx import fields, Namespace

api = Namespace('Atletas', description='Gestion de atletas', path='/atletas')

# Modelo de payload esperado (lo que se envía en el body del POST)
payload_register = api.model('RegistroAtleta', {
    "nombres": fields.String(required=True, description="Nombres del atleta"),
    "apellidos": fields.String(required=True, description="Apellidos del atleta"),
    "cedula": fields.String(required=True, description="Cédula del atleta"),
    "fecha_nacimiento": fields.String(required=True, description="Fecha de nacimiento en formato YYYY-MM-DD"),
    "direccion": fields.String(required=True, description="Dirección del atleta"),
    "telefono": fields.String(required=True, description="Teléfono del atleta"),
    "email": fields.String(required=True, description="Correo electrónico"),
    "username": fields.String(required=True, description="Nombre de usuario para login"),
    "password": fields.String(required=True, description="Contraseña para login"),
})

# Modelos de respuesta
respuesta_success = api.model('RespuestaRegistroSuccess', {
    "Success": fields.String(description="Mensaje de éxito")
})

respuesta_error = api.model('RespuestaRegistroError', {
    "Error": fields.String(description="Mensaje de error")
})
