from dotenv import load_dotenv
from flask import Flask
from app.models import db
from app.config import config
from app.routes.usuarios_routes import usuario
from app.routes.roles_routes import roles
from app.routes.auth_routes import auth_bp
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

load_dotenv(override=True) # Recarga las variables de entorno desde el archivo .env
import os
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    app.register_blueprint(usuario)
    app.register_blueprint(roles)
    app.register_blueprint(auth_bp)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    return app
