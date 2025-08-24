
class ClubBase:
    def __init__(self, clubs):
        self.club  = clubs


class Clubs(ClubBase):
    def __init__(self, clubs):
        super().__init__(clubs)

    def register_club_id(self,nombre, administrador, email,telefono):
        return self.club.register_club(nombre, administrador, email,telefono)
    
    def register_user_club_class(self,id_usuario, id_club, id_rol):
        return self.club.register_user_club(id_usuario, id_club, id_rol)
    
    def formulario_inscripcion(self, formulario,id_club):
        return self.club.crear_formulario_de_inscripcion(formulario,id_club)
    

class ObtenerFormulario(ClubBase):
    def __init__(self, clubs):
        super().__init__(clubs)

    def ver_formularios(self,id_club):
        return self.club.formulario_club(id_club)