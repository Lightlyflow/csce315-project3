from api.db import employee_querier


def clockInHelper(employeeID: int, activity: str):
    """Clock in, rounding to the nearest quarter-hour"""
    employee_querier.clockIn(employeeID, activity)


def clockOutHelper(employeeID: int):
    """Clock out, rounding to the nearest quarter-hour"""
    employee_querier.clockOut(employeeID)

def getWeek1(employeeID, lastweekDate, currDate):
    employee_querier.getWeek1(employeeID, lastweekDate, currDate)

def getWeek2(employeeID, secondLastWeekDate, lastWeekDate):
    employee_querier.getWeek2(employeeID, secondLastWeekDate, lastWeekDate)
