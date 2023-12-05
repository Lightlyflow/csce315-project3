from flask import Blueprint, request, abort, jsonify
from datetime import datetime, timedelta

from .timesheet_helper import clockInHelper, clockOutHelper, getWeek

timesheetAPIBlueprint = Blueprint("timesheet", __name__)


@timesheetAPIBlueprint.route("/clockIn", methods=['POST'])
def clockIn():
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
    data = request.get_json()
    employeeID = -1

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    clockOutHelper(employeeID)
    return "Clocked out", 201


@timesheetAPIBlueprint.route("/week", methods=['POST'])
def week1():
    data = request.get_json()
    employeeID = -1
    currDate = datetime.today() + timedelta(days=1)
    lastWeekDate = datetime.today() - timedelta(days=7)

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getWeek(employeeID, lastWeekDate, currDate))
