from app.models import db

class Usuario(db.Model):
    
    __table_name__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"Usuario='{self.nombre}', email='{self.email}', fecha='{self.created_at}'"

