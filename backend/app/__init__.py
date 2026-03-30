from dotenv import load_dotenv
from flask import Flask
from app.models import db
from app.config import config
from app.routes.usuarios_routes import usuario

load_dotenv(override=True) # Recarga las variables de entorno desde el archivo .env
import os

def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    app.register_blueprint(usuario)
    db.init_app(app)
    return app
