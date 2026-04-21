import os
import sys

# Añadir el directorio actual al path por si acaso
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.extensions import db
from app.models.service import Service
from app.models.dentist import Dentist

def seed_database():
    """Función para poblar la base de datos con servicios y dentistas iniciales"""
    print("🌱 Iniciando seeding de la base de datos...")
    
    # 1. Crear servicios
    services = [
        Service(name="General Checkup", duration=60, description="Evaluación completa"),
        Service(name="Blanqueamiento Láser", duration=90, description="Tratamiento estético"),
        Service(name="Ortodoncia", duration=45, description="Alineación dental"),
        Service(name="Urgencias", duration=30, description="Atención inmediata"),
    ]

    # 2. Crear dentistas
    dentists = [
        Dentist(name="Dr. Vance", specialty="Clínico General"),
        Dentist(name="Dr. Thorne", specialty="Periodoncista"),
        Dentist(name="Dr. Lim", specialty="Estética Dental"),
    ]

    try:
        db.session.add_all(services + dentists)
        db.session.commit()
        print("✅ Base de datos sembrada con éxito 🚀")
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error al sembrar la base de datos: {e}")

if __name__ == "__main__":
    # Esto permite seguir ejecutando python seed.py manualmente si quieres
    app = create_app()
    with app.app_context():
        seed_database()