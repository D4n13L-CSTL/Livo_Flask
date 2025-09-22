from flask import request
from app.auth.db import User
from app.entrenador.db import RegisterEntrenador


class registerEntrenadorService:
    def __init__(self, user_dao: User, entrenador_dao: RegisterEntrenador):
        self.user_dao = user_dao
        self.entrenador_dao = entrenador_dao

        
    def register_entrenador(self,username, email, password, tipo_de_user_id,id_club,id_rol):
        
        id_user = self.user_dao.user_create(username, email, password, tipo_de_user_id)
        
        return self.entrenador_dao.entrenador_club(id_user,id_club, id_rol)
    