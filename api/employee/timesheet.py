from flask import Blueprint, request, abort, jsonify
from datetime import datetime, timedelta

from .timesheet_helper import clockInHelper, clockOutHelper, getWeek

timesheetAPIBlueprint = Blueprint("timesheet", __name__)


@timesheetAPIBlueprint.route("/clockIn", methods=['POST'])
def clockIn():
    """Clocks in an employee based on their ID."""
    data = request.get_json()
    employeeID = -1
    activity = ""

    try:
        employeeID = int(data['employeeid'])
        activity = data['activity']
    except (ValueError, KeyError):
        abort(400)

    clockInHelper(employeeID, activity)
    return "Clocked in", 201


@timesheetAPIBlueprint.route("/clockOut", methods=['POST'])
def clockOut():
    """Clocks out an employee based on their ID."""
    data = request.get_json()
    employeeID = -1

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    clockOutHelper(employeeID)
    return "Clocked out", 201


@timesheetAPIBlueprint.route("/week", methods=['POST'])
def week():
    """Retrieves a week of activity for a specific employee based on their ID."""
    data = request.get_json()
    employeeID = -1
    billingPeriod = ""

    try:
        employeeID = int(data['employeeid'])
        billingPeriod = data['billingperiod']
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getWeek(employeeID, billingPeriod))
