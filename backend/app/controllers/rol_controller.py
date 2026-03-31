from sqlalchemy.exc import IntegrityError
from app.models.rol import Rol
from app.models import db
from flask import jsonify, Response
from app.controllers import Controller

class RolController(Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        roles_list = db.session.execute(db.select(Rol).order_by(db.desc(Rol.id))).scalars().all()
        if roles_list:
            roles_to_dic = [rol.to_dict() for rol in roles_list]
            return jsonify(roles_to_dic), 200
        return jsonify({'message':'No se encontraron roles'}), 404

    @staticmethod
    def show(id: int) -> tuple[Response, int]:
        role = db.session.get(Rol, id)
        if role:
            return jsonify(role.to_dict()), 200
        return jsonify({'message':'Rol no encontrado'}), 404

    @staticmethod
    def create(request: dict) -> tuple[Response, int]:
        nombre:str | None = request.get('nombre')
        error = None
        if not nombre:
            error = 'El nombre es requerido'
        if error is None:
            try:
                rol = Rol(nombre=nombre)
                db.session.add(rol)
                db.session.commit()
                return jsonify({'message':'Rol creado exitosamente'}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message':'Rol ya registrado'}), 409

        return jsonify({'message':error}), 422

    @staticmethod
    def update(request: dict, id: int) -> tuple[Response, int]:
        role = db.session.get(Rol, id)
        if role:
            nombre:str | None = request.get('nombre')
            error = None
            if not nombre:
                error = 'El nombre es requerido'
            if error is None:
                try:
                    role.nombre = nombre
                    db.session.commit()
                    return jsonify({'message':'Rol actualizado exitosamente'}), 200
                except IntegrityError:
                    db.session.rollback()
                    return jsonify({'message':'Rol ya registrado'}), 409
            return jsonify({'message':error}), 422
        return jsonify({'message':'Rol no encontrado'}), 404

    @staticmethod
    def destroy(id: int) -> tuple[Response, int]:
        role = db.session.get(Rol, id)
        if role:
            db.session.delete(role)
            db.session.commit()
            return jsonify({'message':'Rol eliminado exitosamente'}), 200
        return jsonify({'message':'Rol no encontrado'}), 404
