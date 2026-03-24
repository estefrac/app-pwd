
from app import create_app
from app.models import db
from app.models.user import Usuario

app = create_app()

with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos
    print("Tablas creadas exitosamente.")
