from modelClass.BaseDAO import WriteDAO, BaseDAO

class loginUser(BaseDAO):

    def login_user(self,username):

        query = """SELECT username,password from usuarios WHERE username = %s
                    """

        return self.fetch_all(query, (username,))
