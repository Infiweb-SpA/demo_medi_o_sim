from flask import Flask
from .extensions import db
from .routes.main import main_bp
from .routes.booking_bp import booking_bp
from .routes.contact import contact_bp

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinic.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(booking_bp, url_prefix="/booking")
    app.register_blueprint(contact_bp, url_prefix="/contact")

    with app.app_context():
        db.create_all()

    return app