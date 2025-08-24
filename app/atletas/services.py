
class Atletas:
    def __init__(self, atleta):
        self.atleta = atleta
        
    def register_atleta(self,users_atleta,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email):
        self.atleta.register_atleta(users_atleta,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email)
        return {"Success":"Atleta Registrado exitosamente"}