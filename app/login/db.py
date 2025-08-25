from modelClass.BaseDAO import WriteDAO, BaseDAO

class loginUser(BaseDAO):

    def login_user(self,username):

        query = """
        select clubes_usuarios.id_club, usuarios.username, usuarios.password from usuarios
        join clubes_usuarios on usuarios.id = clubes_usuarios.id_usuario
        where usuarios.username =%s
                """

        return self.fetch_all(query, (username,))
