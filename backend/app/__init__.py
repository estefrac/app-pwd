from dotenv import load_dotenv
from flask import Flask
from app.models import db
from app.config import config

load_dotenv(override=True) # Recarga las variables de entorno desde el archivo .env
import os

def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    @app.route('/')
    @app.route('/<nombre>')
    def home(nombre=None):
        if (nombre == None):
            return f' <h1>Hola desde Programación Web Dinámica 2026<h1>'
        return f' <h1>Hola {nombre} te saludamos desde Programación Web Dinámica<h1>'

    @app.route('/saludo')
    def saludo():
        return f' <h1>Saludo desde Programación Web Dinámica 2026<h1>'
    db.init_app(app)
    return app
