from app.controllers.rol_controller import RolController
from flask import Blueprint, request

roles = Blueprint('roles', __name__, url_prefix='/roles')

@roles.route('/')
def get_all():
    return RolController.get_all()

@roles.route('/<int:id>')
def show(id):
    return RolController.show(id)

@roles.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if data is None:
        return {'message': 'No se proporcionaron datos'}, 400
    return RolController.create(data)

@roles.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if data is None:
        return {'message': 'No se proporcionaron datos'}, 400
    return RolController.update(data, id)

@roles.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    return RolController.destroy(id)
