import datetime

from api.db import manager_payroll_querier


def getTimesheet():
    result = manager_payroll_querier.getTimesheet()
    return result if result is not None else []


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    manager_payroll_querier.addTimesheetEntry(employeeID, activity, clockIn, clockOut)


def updateTimesheetEntry(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    manager_payroll_querier.updateTimesheetEntryByID(entryID, employeeID, activity, clockIn, clockOut)


def deleteTimesheetEntry(entryID: int):
    manager_payroll_querier.deleteTimesheetEntry(entryID)


def getEmployees():
    result = manager_payroll_querier.getEmployees()
    return result if result is not None else []


def getBillingPeriods(sinceYear: int = 2023, sinceMonth: int = 10, sinceDay: int = 30):
    startDate = _nextMonday(datetime.date(sinceYear, sinceMonth, sinceDay))
    endDate = _nextMonday(datetime.date.today())

    billingPeriods = []

    while startDate < endDate:
        billingPeriods.append(startDate.isoformat())
        startDate += datetime.timedelta(days=14)

    return billingPeriods


def _nextMonday(date: datetime.date):
    return date + datetime.timedelta((0 - date.weekday()) % 7)
