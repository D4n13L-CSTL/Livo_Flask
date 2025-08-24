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
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            access_token = create_access_token(identity=username)
            resp = make_response(jsonify({"Auth": True}), 200)
            resp.set_cookie(
                "access_token_cookie",
                access_token,
                httponly=True,
                secure=False,   # True en producción con HTTPS
                samesite="Strict"
            )
            return resp
        else:
            return {"Auth": "Contraseña Incorrecta"}, 401