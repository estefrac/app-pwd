from app.models.user import Usuario
from app.models import db
from app.models.rol import Rol
from flask import Response, jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

class AuthController:
    @staticmethod
    def Register(request:dict) -> tuple[Response, int]:
        nombre:str | None = request.get('nombre')
        email:str | None = request.get('email')
        password:str | None = request.get('password')

        error:str | None = None
        if not nombre:
            error = 'El nombre es requerido'
        if not email:
            error = 'El email es requerido'
        if not password:
            error = 'La contraseña es requerida'

        if error is None:
            try:
                rol_user = db.session.execute(db.select(Rol).filter_by(nombre='user')).scalar_one_or_none()
                if rol_user and nombre and password and email is not None:
                    usuario = Usuario(nombre=nombre, email=email, rol_id=rol_user.id, password=password)
                    usuario.generate_password(password)
                    db.session.add(usuario)
                    db.session.commit()
                return jsonify({'message':'Usuario creado exitosamente'}), 201

            except IntegrityError:
                db.session.rollback()
                return jsonify({'message':'Usuario ya registrado'}), 409
        return jsonify({'message':error}), 422

    @staticmethod
    def login(request:dict) -> tuple[Response, int]:

        nombre:str | None = request.get('nombre')
        password:str | None = request.get('password')

        error:str | None = None
        if not nombre:
            error = 'El nombre es requerido'
        if not password:
            error = 'La contraseña es requerida'

        if error is None:
            usuario = db.session.execute(db.select(Usuario).filter_by(nombre=nombre)).scalar_one_or_none()
            if usuario and usuario.validate_password(password):
                access_token = create_access_token(identity=usuario.id, additional_claims={'rol': usuario.rol.nombre if usuario.rol else None})
                return jsonify({'access_token': access_token, 'rol': usuario.rol.nombre if usuario.rol else None, 'nombre': usuario.nombre}), 200
            return jsonify({'message':'Credenciales inválidas'}), 401
        return jsonify({'message':error}), 422
    
