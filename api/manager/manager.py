from flask import Blueprint, render_template

managerBlueprint = Blueprint("manager", __name__, template_folder="templates", static_folder="static")


@managerBlueprint.route("/")
def home():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/analytics")
def analytics():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/employees")
def employees():
    return render_template("manager_employees.html")


@managerBlueprint.route("/inventory")
def inventory():
    return render_template("manager_inventory.html")


@managerBlueprint.route("/menu")
def menu():
    return render_template("manager_menu.html")
