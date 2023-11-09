from flask import Blueprint, render_template
from .manager_helper import getInventory, getLowStock

managerBlueprint = Blueprint("manager", __name__, template_folder="templates", static_folder="static")


@managerBlueprint.route("/", methods=["GET"])
def home():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/analytics", methods=["GET"])
def analytics():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/employees", methods=["GET"])
def employees():
    return render_template("manager_employees.html")


@managerBlueprint.route("/inventory", methods=["GET"])
def inventory():
    allInventory = getInventory()
    lowStock = getLowStock()
    return render_template("manager_inventory.html",
                           inventory=allInventory,
                           lowStock=lowStock)


@managerBlueprint.route("/menu", methods=["GET"])
def menu():
    return render_template("manager_menu.html")


# POST Endpoints

