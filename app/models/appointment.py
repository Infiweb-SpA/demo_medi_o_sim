from app.extensions import db
from datetime import datetime

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    date = db.Column(db.Date)
    time = db.Column(db.String(20))

    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
    dentist_id = db.Column(db.Integer, db.ForeignKey("dentist.id"))