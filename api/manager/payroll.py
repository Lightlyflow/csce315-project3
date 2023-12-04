from flask import Blueprint, abort, jsonify, request

from .payroll_helper import getTimesheet, addTimesheetEntry, updateTimesheetEntry, deleteTimesheetEntry

payrollAPIBlueprint = Blueprint("payroll", __name__)


@payrollAPIBlueprint.route("/timesheet", methods=['GET'])
def timesheet():
    return jsonify(getTimesheet())


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
        clockOut = data['clockOut']
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
        clockOut = data['clockOut']
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
