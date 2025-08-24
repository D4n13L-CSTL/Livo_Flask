
class Clubs:
    def __init__(self, clubs):
        self.club  = clubs

    def register_club_id(self,nombre, administrador, email,telefono):
        return self.club.register_club(nombre, administrador, email,telefono)
    
    def register_user_club_class(self,id_usuario, id_club, id_rol):
        return self.club.register_user_club(id_usuario, id_club, id_rol)
        
    