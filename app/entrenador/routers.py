from .documentation import *
from flask_restx import Resource

@api.route('')
class ClaseRouterEntrenador(Resource):
    def get(self):
        return {"A":1}