from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    from app.models.user import Usuario
    from app.models.rol import Rol
    db.create_all()
    print('las tablas se crearon correctamente')
