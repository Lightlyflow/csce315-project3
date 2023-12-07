from flask import Blueprint, abort, jsonify, request
from flask_login import current_user

from .payroll_helper import getTimesheet, addTimesheetEntry, updateTimesheetEntry, deleteTimesheetEntry, \
    getTimesheetByID, getTotalHours, getPayRate, payEmployeeByID

payrollAPIBlueprint = Blueprint("payroll", __name__)


@payrollAPIBlueprint.before_request
def checkAdmin():
    """
    Checks if the current user is an admin.
    :return: 403 if user is not admin
    """
    if current_user.is_authenticated and current_user.isAdmin:
        return
    abort(403)


@payrollAPIBlueprint.route("/timesheet", methods=['GET', 'POST'])
def timesheet():
    """Sets up an endpoint for the timesheet.
    Returns Response of the default timesheet
    or a specific employee's timesheet."""
    if request.method == 'GET':
        return jsonify(getTimesheet())
    elif request.method == 'POST':
        data = request.get_json()

        try:
            employeeID = int(data['employeeid'])
            billingPeriod = data['billingperiod']
        except (ValueError, KeyError):
            abort(400)

        return jsonify(getTimesheetByID(employeeID, billingPeriod))
    abort(404)


@payrollAPIBlueprint.route("/add", methods=['POST'])
def timesheetAdd():
    """Sets up an endpoint to add entries to a timesheet."""
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
        activity = data['activity']
        clockIn = data['clockin']
        clockOut = data['clockout']
    except (ValueError, KeyError):
        abort(400)

    addTimesheetEntry(employeeID, activity, clockIn, clockOut)
    return "Added", 201


@payrollAPIBlueprint.route("/update", methods=['POST'])
def timesheetUpdate():
    """Sets up an endpoint to update timesheet entries."""
    data = request.get_json()

    try:
        entryID = int(data['entryid'])
        employeeID = int(data['employeeid'])
        activity = data['activity']
        clockIn = data['clockin']
        clockOut = data['clockout']
    except (ValueError, KeyError):
        abort(400)

    updateTimesheetEntry(entryID, employeeID, activity, clockIn, clockOut)
    return "Updated", 201


@payrollAPIBlueprint.route("/delete", methods=['POST'])
def timesheetDelete():
    """Sets up an endpoint to delete timesheet entries."""
    data = request.get_json()

    try:
        entryID = int(data['entryid'])
    except (ValueError, KeyError):
        abort(400)

    deleteTimesheetEntry(entryID)
    return "Deleted", 201


@payrollAPIBlueprint.route("/hours", methods=['POST'])
def employeeHours():
    """Sets up an endpoint to get an employee's hours.
    Returns a Response of the getTotalHours query."""
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
        billingPeriod = data['billingperiod']
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getTotalHours(employeeID, billingPeriod))


@payrollAPIBlueprint.route("/payrate", methods=['POST'])
def employeePayRate():
    """Sets up an endpoint to get an employee's pay rate.
    Returns a Response of the getPayRate query."""
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getPayRate(employeeID))


@payrollAPIBlueprint.route("/pay", methods=['POST'])
def payEmployee():
    """Sets up an endpoint to pay employees by id."""
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
        totalPayment = int(data['total'])
    except (ValueError, KeyError):
        abort(400)
    if payEmployeeByID(employeeID, totalPayment):
        return jsonify("Payment succeeded!")
    return jsonify("Payment failed!")
