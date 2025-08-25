from flask import Flask
from config import settings
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager

from app.auth.routers import bp as auth_bp, api as api_auth
from app.atletas.routers import atleta_bp, api as api_atleta
from app.clubs.routers import club_bp, api as api_club
from app.login.routers import login_bp, api as api_login


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

    CORS(app, supports_credentials=True, origins=["https://livo.loca.lt" , "http://10.100.39.23:3000"])
    api = Api(app, 
              doc='/docs',
              title='Livo Flask')


    app.register_blueprint(auth_bp)
    app.register_blueprint(atleta_bp)
    app.register_blueprint(club_bp)
    app.register_blueprint(login_bp)
    
    api.add_namespace(api_auth)
    api.add_namespace(api_atleta)
    api.add_namespace(api_club)
    api.add_namespace(api_login)
    

    return app
