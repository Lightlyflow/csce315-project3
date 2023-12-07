from flask import Blueprint, render_template, request, jsonify, abort, redirect, url_for
from flask_login import login_required, current_user

from .employee_helper import getMenuCategories, getToppingData, placeOrder, getWeather, getMenuData
from .orders import ordersAPIBlueprint
from .timesheet import timesheetAPIBlueprint
from .timesheet_helper import getBillingPeriods

employeeBlueprint = Blueprint("employee", __name__, template_folder="templates", static_folder="static")


@employeeBlueprint.before_request
@login_required
def requireLogin():
    """
    Aborts if an unauthorized user attempts to access employee or manager pages.
    :return: 403 if not employee
    """
    if not current_user.is_authenticated:
        abort(403)
    if not current_user.isEmployee:
        abort(403)


@employeeBlueprint.route("/", methods=['GET'])
def home():
    """
    Redirects to employee timesheet page
    :return: redirect to employee timesheet
    """
    return redirect(url_for("employee.timesheet"))


@employeeBlueprint.route("/order", methods=['GET'])
def cashier():
    """
    Stores menu item, category, topping and weather information before rendering the employee home page.
    :return: Render of cashier page
    """
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
    """
    Retrieves any items that were previously saved.
    :return: Response containing previously saved items
    """
    data = request.get_json()
    if 'savedMenuItems' in data:
        savedItems = data['savedMenuItems']
        placeOrder(savedItems)
        return jsonify({'message': 'Data received successfully'})

    return jsonify({'error': 'Invalid format'})


@employeeBlueprint.route("/timesheet", methods=['GET'])
def timesheet():
    """
    Renders employee timesheet page.
    :return: render of employee timesheet
    """
    return render_template("employee_timesheet.html", billingPeriods=getBillingPeriods())


@employeeBlueprint.route("/orders", methods=['GET'])
def orders():
    """
    Renders employee order management page
    :return: render of employee order management page
    """
    return render_template("employee_orders.html")


# Other blueprints
employeeBlueprint.register_blueprint(timesheetAPIBlueprint, url_prefix="/timesheet")
employeeBlueprint.register_blueprint(ordersAPIBlueprint, url_prefix="/orders")
