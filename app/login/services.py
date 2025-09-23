import bcrypt
from flask import make_response, jsonify
from flask_jwt_extended import create_access_token,get_csrf_token,set_access_cookies


class LoginAuth:
    def __init__(self, login_user_dao):
        self.login_user_dao = login_user_dao

    def login_user_service(self, username: str, password: str):
        user = self.login_user_dao.login_user(username)
        if not user:
            return {"Auth": "Usuario No encontrado"}, 404

        stored_password = user[0]['password'].encode('utf-8')
        id_club = user[0]['id_club']
        id_club_atleta = user[0]['id_club_perteniciente']
        tipo_de_user = user[0]['tipo_de_user']
        id_atleta = user[0]['id_atleta']
        id_usuario= user[0]['id_usuario']

        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            access_token = create_access_token(identity=username)
            resp = make_response(jsonify({"Success": True , "csrf_token": get_csrf_token(access_token)},), 200)
            #CAMBIAR EL SECURE A TRUE CUANDO HAYA REALIZADO EL MODULO
            set_access_cookies(resp, access_token,domain="bright-clocks-raise.loca.lt")
           
            resp.set_cookie(
                "tipo_de_user",
                tipo_de_user,
                httponly=True,
                secure=True, 
                samesite="None",
                max_age=36000 ,
                domain="bright-clocks-raise.loca.lt"
            )
            resp.set_cookie(
                "id_usuario",
                str(id_usuario),
                httponly=True,
                secure=True, 
                samesite="None",
                max_age=36000 ,
                domain="bright-clocks-raise.loca.lt"
            )

            
            if tipo_de_user == 'ADMINISTRADOR':
                resp.set_cookie(
                    "id_club_cookie",
                    str(id_club),
                    httponly=True,
                    secure=True,   # True en producción con HTTPS
                    samesite="None",
                    max_age=36000 ,
                domain="bright-clocks-raise.loca.lt"
                )  
            elif tipo_de_user == 'ATLETA':
                resp.set_cookie(
                    "id_club_atleta_cookie", #GUARDA EL ID DEL CLUB QUE PERTNECE EL ATLETA
                    str(id_club_atleta),
                    httponly=True,
                    secure=True, 
                    samesite="None",
                    max_age=36000 ,
                domain="bright-clocks-raise.loca.lt"
                )
                resp.set_cookie(
                "id_atleta",
                str(id_atleta),
                httponly=True,
                secure=True,
                samesite="None",
                max_age=36000 ,
                domain="bright-clocks-raise.loca.lt"
                )
            
            return resp
        else:
            return {"Auth": "Contraseña Incorrecta"}, 401
        
