from flask import Blueprint, render_template

managerBlueprint = Blueprint("manager", __name__, template_folder="templates")


@managerBlueprint.route("/")
def home():
    return render_template("manager_home.html")
