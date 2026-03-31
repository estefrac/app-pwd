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
    data = request.get_json()
    if data is None:
        return {'message': 'No se proporcionaron datos'}, 400
    return UsuarioController.create(data)

@usuario.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if data is None:
        return {'message': 'No se proporcionaron datos'}, 400
    return UsuarioController.update(data, id)

@usuario.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    return UsuarioController.destroy(id)
