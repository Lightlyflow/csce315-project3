from flask import Blueprint, request, abort, jsonify
from datetime import datetime, timedelta

from .timesheet_helper import clockInHelper, clockOutHelper, getWeek1, getWeek2

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


@timesheetAPIBlueprint.route("/week1", methods=['POST'])
def week1():
    data = request.get_json()
    employeeID = -1
    currDate = datetime.today() + timedelta(days=1)
    lastWeekDate = datetime.today() - timedelta(days=7)

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getWeek1(employeeID, lastWeekDate, currDate))


@timesheetAPIBlueprint.route("/week2", methods=['POST'])
def week2():
    data = request.get_json()
    employeeID = -1
    lastWeekDate = datetime.today() - timedelta(days=7)
    secondLastWeekDate = datetime.today() - timedelta(days=14)

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    return jsonify(getWeek2(employeeID, secondLastWeekDate, lastWeekDate))
