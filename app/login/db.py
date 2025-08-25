from modelClass.BaseDAO import WriteDAO, BaseDAO

class loginUser(BaseDAO):

    def login_user(self,username):

        query = """
            select clubes_usuarios.id_club,tipo_de_user.nombre as tipo_de_user, usuarios.username, usuarios.password from usuarios
            left join atletas on atletas.id_usuario = usuarios.id
            join tipo_de_user on usuarios.tipo_de_user_id = tipo_de_user.id
            left join clubes_usuarios on usuarios.id = clubes_usuarios.id_usuario
            where usuarios.username =%s
                """

        return self.fetch_all(query, (username,))
