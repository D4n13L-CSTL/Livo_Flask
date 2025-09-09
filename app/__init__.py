from flask import Flask
from config import settings
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager

from app.auth.routers import  api as api_auth
from app.atletas.routers import   api as api_atleta
from app.clubs.routers import  api as api_club
from app.login.routers import  api as api_login
from app.gestion_eventos.routers import  api as api_gestion_eventos
from app.pagos_atletas_club.routers import  api as api_gestion_pago_atletas

def create_app():
    app = Flask(__name__)
    app.config['SESSION_COOKIE_NAME'] = 'session'
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.config['DEBUG'] = settings.DEBUG
    app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
    app.config["JWT_TOKEN_LOCATION"] = settings.JWT_TOKEN_LOCATION
    app.config["JWT_COOKIE_SECURE"] = settings.JWT_COOKIE_SECURE
    app.config["JWT_COOKIE_HTTPONLY"] = settings.JWT_COOKIE_HTTPONLY
    app.config["JWT_COOKIE_SAMESITE"] =  settings.JWT_COOKIE_SAMESITE

    jwt = JWTManager(app)

    CORS(app, supports_credentials=True, origins=["https://livosport.loca.lt" , "http://10.100.39.42:3000","http://10.100.39.23:3000"])
    api = Api(app, 
              doc='/docs',
              title='Livo Flask')


    
    
    api.add_namespace(api_auth)
    api.add_namespace(api_atleta)
    api.add_namespace(api_club)
    api.add_namespace(api_login)
    api.add_namespace(api_gestion_eventos)
    api.add_namespace(api_gestion_pago_atletas)
    

    return app
