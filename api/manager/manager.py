import json

from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import login_required, current_user

from .inventory import inventoryAPIBlueprint
from .inventory_helper import getInventory, getLowStock
from .analytics import analyticsAPIBlueprint
from .menu import menuAPIBlueprint
from .user_management import userManagementBlueprint
from .orders import ordersAPIBlueprint
from .payroll import payrollAPIBlueprint
from .payroll_helper import getEmployees, getBillingPeriods
from .image import imageAPIBlueprint

managerBlueprint = Blueprint("manager", __name__, template_folder="templates", static_folder="static")


@managerBlueprint.before_request
@login_required
def requireLogin():
    """Checks to ensure the user is authenticated."""
    if not current_user.is_authenticated or not current_user.isManager:
        abort(403)


@managerBlueprint.route("/", methods=["GET"])
def home():
    """Sets up an endpoint for the default manager page."""
    return redirect(url_for('manager.analytics'))


@managerBlueprint.route("/analytics", methods=["GET"])
def analytics():
    """Sets up an endpoint for the manager analytics page."""
    return render_template("manager_analytics.html")


@managerBlueprint.route("/user_management", methods=["GET"])
def employees():
    """Sets up an endpoint for the manager user management page."""
    return render_template("manager_user_management.html")


@managerBlueprint.route("/inventory", methods=["GET"])
def inventory():
    """Sets up an endpoint for the manager inventory page."""
    allInventory = getInventory()
    lowStock = getLowStock()
    return render_template("manager_inventory.html",
                           inventory=allInventory,
                           lowStock=lowStock)


@managerBlueprint.route("/menu", methods=["GET"])
def menu():
    """Sets up an endpoint for the manager menu page."""
    return render_template("manager_menu.html")


@managerBlueprint.route("/orders", methods=['GET'])
def orders():
    """Sets up an endpoint for the manager orders page."""
    return render_template("manager_orders.html")


@managerBlueprint.route("/payroll", methods=['GET'])
def payroll():
    """Sets up an endpoint for the manager payroll page."""
    employeeList = getEmployees()
    billingPeriods = getBillingPeriods()
    return render_template("manager_payroll.html",
                           employees=employeeList,
                           billingPeriods=billingPeriods)


# POST Endpoints
managerBlueprint.register_blueprint(inventoryAPIBlueprint, url_prefix='/inventory')
managerBlueprint.register_blueprint(analyticsAPIBlueprint, url_prefix='/analytics')
managerBlueprint.register_blueprint(menuAPIBlueprint, url_prefix='/menu')
managerBlueprint.register_blueprint(userManagementBlueprint, url_prefix='/user_management')
managerBlueprint.register_blueprint(ordersAPIBlueprint, url_prefix='/orders')
managerBlueprint.register_blueprint(payrollAPIBlueprint, url_prefix='/payroll')
managerBlueprint.register_blueprint(imageAPIBlueprint, url_prefix="/images")
