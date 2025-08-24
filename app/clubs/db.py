from modelClass.BaseDAO import WriteDAO, BaseDAO

class Clubes(WriteDAO):

    def register_club(self,nombre, administrador, email,telefono):

        query = """
        INSERT INTO clubes (nombre, administrador, email,telefono) VALUES (%s,%s,%s,%s) RETURNING id
                    """

        return self.insert_and_return_id(query, (nombre, administrador, email,telefono))
    
    def register_user_club(self,id_usuario, id_club, id_rol):
        query = """
                INSERT INTO clubes_usuarios (id_usuario, id_club, id_rol) VALUES (%s,%s,%s)
            """
        return self.execute(query, (id_usuario, id_club, id_rol))