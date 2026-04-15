from flask import Blueprint, render_template, request, redirect
from app.models.inquiry import Inquiry
from app.extensions import db

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        inquiry = Inquiry(
            name=request.form["name"],
            email=request.form["email"],
            subject=request.form["subject"],
            message=request.form["message"]
        )
        db.session.add(inquiry)
        db.session.commit()

        return redirect("/contact")

    return render_template("contact.html")