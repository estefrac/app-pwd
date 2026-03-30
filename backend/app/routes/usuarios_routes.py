# Aca se definen las rutas relacionadas con los usuarios, como el registro, inicio de sesión, etc. Se importan los controladores necesarios para manejar las solicitudes y se utiliza Blueprint para organizar las rutas de manera modular.
from app.controllers.user_controller import UsuarioController
from flask import Blueprint, request

usuario = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario.route('/')
def get_all():
    return UsuarioController.get_all()

@usuario.route('/<int:id>')
def show(id):
    return UsuarioController.show(id)

@usuario.route('/', methods=['POST'])
def create():
    return UsuarioController.create(request.get_json())
