from modelClass.BaseDAO import BaseDAO, WriteDAO

class RegisterEntrenador(WriteDAO):
    
    def entrenador_club(self,id_usuario, id_club, id_rol):
        query = """
        insert into clubes_usuarios (id_usuario, id_club, id_rol) VALUES(%s,%s,%s)
                """
        
        return self.execute(query,(id_usuario, id_club, id_rol))