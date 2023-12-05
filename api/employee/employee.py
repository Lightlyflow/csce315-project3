from flask import Blueprint, render_template, request, jsonify, abort
from flask_login import login_required, current_user

from .employee_helper import getMenuCategories, getToppingData, placeOrder, getWeather, getMenuData
from .timesheet import timesheetAPIBlueprint
from .timesheet_helper import getBillingPeriods

employeeBlueprint = Blueprint("employee", __name__, template_folder="templates", static_folder="static")


@employeeBlueprint.before_request
@login_required
def requireLogin():
    if not current_user.is_authenticated:
        abort(403)


@employeeBlueprint.route("/", methods=['GET'])
def home():
    # Menu items dynamic loading
    menuQuery = getMenuData()
    menuCategories = getMenuCategories()
    menuItems = {category: [(item[0], item[2], item[3]) for item in menuQuery if item[1] == category] for category in
                 menuCategories}

    # Weather api work to get temp and conditions
    weather = getWeather()
    temperature = weather[0]
    conditions = weather[1]

    # Toppings
    toppingNames = getToppingData()

    return render_template("employee_home.html", menuCategories=menuCategories, menuItems=menuItems,
                           toppingNames=toppingNames, temperature=temperature, conditions=conditions)


@employeeBlueprint.route("/post_endpoint", methods=['POST'])
def receive_saved_items():
    data = request.get_json()
    if 'savedMenuItems' in data:
        savedItems = data['savedMenuItems']
        placeOrder(savedItems)
        return jsonify({'message': 'Data received successfully'})

    return jsonify({'error': 'Invalid format'})


@employeeBlueprint.route("/timesheet", methods=['GET'])
def timesheet():
    return render_template("employee_timesheet.html", billingPeriods=getBillingPeriods())


# Other blueprints
employeeBlueprint.register_blueprint(timesheetAPIBlueprint, url_prefix="/timesheet")
