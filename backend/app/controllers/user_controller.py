from app.models.user import Usuario
from app.models import db
from app.controllers import Controller
from flask import jsonify, Response
from sqlalchemy.exc import IntegrityError

class UsuarioController(Controller):
    
    @staticmethod
    def get_all():
        usuarios_list = db.session.execute(db.select(Usuario).order_by(db.desc(Usuario.id))).scalars().all()
        if usuarios_list:
            usuarios_to_dic = [usuario.to_dict() for usuario in usuarios_list]
            return jsonify(usuarios_to_dic), 200
        return jsonify({'message':'No se encontraron usuarios'}), 404

    @staticmethod
    def show(id):
        usuario = db.session.get(Usuario, id)
        if usuario:
            return jsonify(usuario.to_dict()), 200
        return jsonify({'message':'Usuario no encontrado'}), 404

    @staticmethod
    def create(request:dict) -> tuple[Response, int]:
        nombre = request.get('nombre')
        email = request.get('email')
        error = None
        if not nombre:
            error = 'El nombre es requerido'
        if not email:
            error = 'El email es requerido'
        if error is None:
            try:
                usuario = Usuario(nombre=nombre, email=email)
                db.session.add(usuario)
                db.session.commit()
                return jsonify({'message':'Usuario creado exitosamente'}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message':'Usuario ya registrado'}), 409
        return jsonify({'message':error}), 422

    @staticmethod
    def update(request: dict, id: int) -> tuple[Response, int]:
        usuario = db.session.get(Usuario, id)
        if usuario:
            nombre = request.get('nombre')
            email = request.get('email')
            error = None
            if not nombre:
                error = 'El nombre es requerido'
            if not email:
                error = 'El email es requerido'
            if error is None:
                try:
                    usuario.nombre = nombre
                    usuario.email = email
                    db.session.commit()
                    return jsonify({'message':'Usuario actualizado exitosamente'}), 200
                except IntegrityError:
                    db.session.rollback()
                    return jsonify({'message':'Usuario ya registrado'}), 409
            return jsonify({'message':error}), 422
        return jsonify({'message':'Usuario no encontrado'}), 404

    @staticmethod
    def destroy(id: int) -> tuple[Response, int]:
        usuario = db.session.get(Usuario, id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({'message':'Usuario eliminado exitosamente'}), 200
        return jsonify({'message':'Usuario no encontrado'}), 404
