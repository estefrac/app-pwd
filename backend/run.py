from app import create_app
from app.models import db
from app.models.user import Usuario

app = create_app()

with app.app_context():
    db.create_all()
    print('las tablas se crearon correctamente')
