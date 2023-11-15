from flask import Blueprint, render_template
from flask_login import login_required

from .inventory import inventoryAPIBlueprint
from .inventory_helper import getInventory, getLowStock
from .analytics import analyticsAPIBlueprint
from .analytics_helper import getPairReport

managerBlueprint = Blueprint("manager", __name__, template_folder="templates", static_folder="static")


@managerBlueprint.before_request
@login_required
def requireLogin():
    pass


@managerBlueprint.route("/", methods=["GET"])
def home():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/analytics", methods=["GET"])
def analytics():
    pairReport = getPairReport()
    print(f"{pairReport =}")
    return render_template("manager_analytics.html", pairReport = pairReport)


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
managerBlueprint.register_blueprint(inventoryAPIBlueprint, url_prefix='/inventory')
managerBlueprint.register_blueprint(analyticsAPIBlueprint, url_prefix='/analytics')
