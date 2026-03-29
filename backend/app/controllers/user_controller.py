from app.models.user import Usuario
from app.models import db
from app.controllers import Constroller
from flask import jsonify
from sqlalchemy.exc import IntegrityError

class UsuarioController(Controller):
    
    @staticmethod
    def get_all():
        usuarios_list = db.session.execute(db.select(Usuarios)).scalar()
        if usuarios_list:
            usuarios_to_dic = [usuario.to_dict() for usuario in usuarios_list]
            return jsonify(usuarios_to_dic), 200
        return jsonify({'message':'No se encontraron usuarios'}), 404
