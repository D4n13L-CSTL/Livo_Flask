
class Atletas:
    def __init__(self, atleta):
        self.atleta = atleta
        
    def register_atleta(self,users_atleta,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email):
        return self.atleta.register_atleta(users_atleta,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email)
    
    def inscripcion_de_atleta(self,id_atleta, id_club):
        return self.atleta.inscripcion_atleta_club(id_atleta, id_club)

    def guardar_informacion_de_atleta(self,id_atleta,id_formulario,respuestas):

        return self.atleta.register_informacion_atleta(id_atleta,id_formulario,respuestas)