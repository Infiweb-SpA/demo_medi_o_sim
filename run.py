import os
from app import create_app
from app.extensions import db
from app.models.service import Service # Importamos un modelo para verificar contenido

app = create_app()

# Configuración automática al arrancar
with app.app_context():
    # 1. Crear tablas si no existen (Equivalente a db.create_all())
    db.create_all()
    
    # 2. Verificar si la base de datos está vacía
    # Si no hay servicios registrados, ejecutamos el seed
    if Service.query.count() == 0:
        print("⚠️ Base de datos vacía detectada. Poblando datos iniciales...")
        from seed import seed_database
        seed_database()
    else:
        print("ℹ️ La base de datos ya contiene información. Omitiendo seed.")

if __name__ == "__main__":
    # Railway suele pasar el puerto por variable de entorno
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)