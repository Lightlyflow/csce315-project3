from flask import Blueprint, render_template

authBlueprint = Blueprint("auth", __name__, template_folder="templates")


@authBlueprint.route("/")
def home():
    return render_template("login.html")
