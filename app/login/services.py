import bcrypt
from flask import make_response, jsonify
from flask_jwt_extended import create_access_token


class LoginAuth:
    def __init__(self, login_user_dao):
        self.login_user_dao = login_user_dao

    def login_user_service(self, username: str, password: str):
        user = self.login_user_dao.login_user(username)
        if not user:
            return {"Auth": "Usuario No encontrado"}, 404

        stored_password = user[0]['password'].encode('utf-8')
        id_club = user[0]['id_club']
        tipo_de_user = user[0]['tipo_de_user']
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            access_token = create_access_token(identity=username)
            resp = make_response(jsonify({"Success": True }), 200)
            resp.set_cookie(
                "access_token_cookie",
                access_token,
                httponly=True,
                secure=True,   # True en producción con HTTPS
                samesite="None"
            )
            resp.set_cookie(
                "tipo_de_user",
                tipo_de_user,
                httponly=True,
                secure=True, 
                samesite="None"
            )
            if tipo_de_user == 'ADMINISTRADOR':
                resp.set_cookie(
                    "id_club_cookie",
                    str(id_club),
                    httponly=True,
                    secure=True,   # True en producción con HTTPS
                    samesite="None"
                )
            
            return resp
        else:
            return {"Auth": "Contraseña Incorrecta"}, 401
        