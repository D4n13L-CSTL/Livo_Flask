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


#/////////////////////////
# Payload esperado para el formulario dinámico
payload_formulario = api.model('Formulario', {
    'id_club': fields.Integer(required=True, description='ID del club al que pertenece el formulario'),
    'formulario': fields.Raw(required=True, description='Diccionario dinámico con pares clave:valor del formulario')
})

# Respuesta exitosa al crear formulario
respuesta_formulario_success = api.model('FormularioSuccess', {
    'Response': fields.String(description='Mensaje de éxito')
})

# Respuesta de error
respuesta_formulario_error = api.model('ErrorResponse', {
    'Error': fields.String(description='Mensaje de error')
})