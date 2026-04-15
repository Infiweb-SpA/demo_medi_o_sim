from app import create_app
from app.extensions import db
from app.models.service import Service
from app.models.dentist import Dentist

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    services = [
        Service(name="General Checkup", duration=60, description="Evaluación completa"),
        Service(name="Blanqueamiento Láser", duration=90, description="Tratamiento estético"),
        Service(name="Ortodoncia", duration=45, description="Alineación dental"),
        Service(name="Urgencias", duration=30, description="Atención inmediata"),
    ]

    dentists = [
        Dentist(name="Dr. Vance", specialty="Clínico General"),
        Dentist(name="Dr. Thorne", specialty="Periodoncista"),
        Dentist(name="Dr. Lim", specialty="Estética Dental"),
    ]

    db.session.add_all(services + dentists)
    db.session.commit()

    print("Base de datos sembrada 🚀")