from conexiones.cursores import get_cursor
from .db import Clubes
from .services import Clubs

club_auth = Clubes(get_cursor)

gestion_club = Clubs(club_auth)