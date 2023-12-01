from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

from .inventory import inventoryAPIBlueprint
from .inventory_helper import getInventory, getLowStock
from .menu import menuAPIBlueprint
from .user_management import userManagementBlueprint
from .orders import ordersAPIBlueprint

managerBlueprint = Blueprint("manager", __name__, template_folder="templates", static_folder="static")


@managerBlueprint.before_request
@login_required
def requireLogin():
    if not current_user.is_authenticated or not current_user.isManager:
        abort(403)


@managerBlueprint.route("/", methods=["GET"])
def home():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/analytics", methods=["GET"])
def analytics():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/user_management", methods=["GET"])
def employees():
    return render_template("manager_user_management.html")


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


@managerBlueprint.route("/orders", methods=['GET'])
def orders():
    return render_template("manager_orders.html")


# POST Endpoints
managerBlueprint.register_blueprint(inventoryAPIBlueprint, url_prefix='/inventory')
managerBlueprint.register_blueprint(menuAPIBlueprint, url_prefix='/menu')
managerBlueprint.register_blueprint(userManagementBlueprint, url_prefix='/user_management')
managerBlueprint.register_blueprint(ordersAPIBlueprint, url_prefix='/orders')
