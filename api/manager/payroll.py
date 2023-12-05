from flask import Blueprint, abort, jsonify, request

from .payroll_helper import getTimesheet, addTimesheetEntry, updateTimesheetEntry, deleteTimesheetEntry, \
    getTimesheetByID, getTotalHours, getPayRate, payEmployeeByID

payrollAPIBlueprint = Blueprint("payroll", __name__)


@payrollAPIBlueprint.route("/timesheet", methods=['GET', 'POST'])
def timesheet():
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
    data = request.get_json()
    employeeID = -1
    activity = ""
    clockIn = ""
    clockOut = ""

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
    data = request.get_json()
    entryID = -1
    employeeID = -1
    activity = ""
    clockIn = ""
    clockOut = ""

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
    data = request.get_json()
    entryID = -1

    try:
        entryID = int(data['entryid'])
    except (ValueError, KeyError):
        abort(400)

    deleteTimesheetEntry(entryID)
    return "Deleted", 201


@payrollAPIBlueprint.route("/hours", methods=['POST'])
def employeeHours():
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
        billingPeriod = data['billingperiod']
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getTotalHours(employeeID, billingPeriod))


@payrollAPIBlueprint.route("/payrate", methods=['POST'])
def employeePayRate():
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getPayRate(employeeID))


@payrollAPIBlueprint.route("/pay", methods=['POST'])
def payEmployee():
    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
        totalPayment = int(data['total'])
    except (ValueError, KeyError):
        abort(400)
    if payEmployeeByID(employeeID, totalPayment):
        return jsonify("Payment succeeded!")
    return jsonify("Payment failed!")
