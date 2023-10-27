from flask import Blueprint, render_template

employeeBlueprint = Blueprint("employee", __name__, template_folder="templates")


@employeeBlueprint.route("/")
def home():
    return render_template("employee_home.html")
