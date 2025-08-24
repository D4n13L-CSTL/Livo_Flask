from conexiones.cursores import get_cursor
from .db import Clubes, VerFormularios
from .services import Clubs, ObtenerFormulario

club_auth = Clubes(get_cursor)
formularios_de_inscripciones = VerFormularios(get_cursor)



gestion_club = Clubs(club_auth)
formularios_registrados = ObtenerFormulario(formularios_de_inscripciones)