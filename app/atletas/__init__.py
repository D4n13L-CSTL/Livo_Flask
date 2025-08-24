from conexiones.cursores import get_cursor
from .db import WriteAleta
from .services import Atletas

atleta = WriteAleta(get_cursor)
register_atletas = Atletas(atleta)