from modelClass.BaseDAO import BaseDAO,WriteDAO

class WriteAleta(WriteDAO):
    def register_atleta(self, id_usario,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email):
        query = """
                INSERT INTO atletas (id_usuario,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        return self.execute(query,(id_usario,nombres,apellidos,cedula,fecha_nacimiento, direccion,telefono, email))
    
    