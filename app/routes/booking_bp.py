from flask import Blueprint, render_template, request, redirect, flash
from app.models.service import Service
from app.models.dentist import Dentist
from app.models.appointment import Appointment
from app.extensions import db
from datetime import datetime

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/", methods=["GET", "POST"])
def booking():
    services = Service.query.all()
    dentists = Dentist.query.all()

    if request.method == "POST":
        try:
            appointment = Appointment(
                patient_name=request.form.get("name", "Paciente"),
                email=request.form.get("email", "paciente@email.com"),
                date=datetime.strptime(request.form["date"], "%Y-%m-%d"),
                time=request.form["time"],
                service_id=request.form["service_id"],
                dentist_id=request.form["dentist_id"]
            )
            db.session.add(appointment)
            db.session.commit()
            flash("¡Cita reservada exitosamente! Te contactaremos pronto.", "success")
            return redirect("/booking")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al reservar: {str(e)}", "error")
            return redirect("/booking")

    return render_template("reservas.html", services=services, dentists=dentists)