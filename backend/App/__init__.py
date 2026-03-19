from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/<nombre>')
    def home(nombre=None):
        if (nombre == None):
            return f' <h1>Hola desde Programación Web Dinámica 2026<h1>'
        return f' <h1>Hola {nombre} te saludamos desde Programación Web Dinámica<h1>'

    @app.route('/saludo')
    def saludo():
        return f' <h1>Saludo desde Programación Web Dinámica 2026<h1>'

    return app
