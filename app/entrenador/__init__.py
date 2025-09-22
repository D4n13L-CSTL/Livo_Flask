from conexiones.cursores import get_cursor
from app.auth.db import User
from .db import RegisterEntrenador
from .services import registerEntrenadorService
user = User(get_cursor)

db_register =  RegisterEntrenador(get_cursor)


services_entrenador = registerEntrenadorService(user, db_register)