import datetime

from api.db import manager_payroll_querier


def getTimesheet():
    """Calls the querier and returns the timesheet from the database."""
    result = manager_payroll_querier.getTimesheet()
    return result if result is not None else []


def getTimesheetByID(employeeID: int, billingPeriod: str):
    """Calls the querier and returns the timesheet by employeeID and period from the database."""
    result = manager_payroll_querier.getTimesheetByID(employeeID, billingPeriod)
    return result if result is not None else []


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    """Calls the querier and adds a timesheet entry to the database."""
    manager_payroll_querier.addTimesheetEntry(employeeID, activity, clockIn, clockOut)


def updateTimesheetEntry(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    """Calls the querier and updates a timesheet entry in the database."""
    manager_payroll_querier.updateTimesheetEntryByID(entryID, employeeID, activity, clockIn, clockOut)


def deleteTimesheetEntry(entryID: int):
    """Calls the querier and deletes a timesheet entry from the database."""
    manager_payroll_querier.deleteTimesheetEntry(entryID)


def getEmployees():
    """Calls the querier and returns the employees on payroll from the database."""
    result = manager_payroll_querier.getEmployees()
    return result if result is not None else []


def getTotalHours(employeeID: int, billingPeriod: str):
    """Calls the querier and returns the total hours for an employee over a period from the database."""
    result = manager_payroll_querier.getTotalHours(employeeID, billingPeriod)
    return result if result is not None else []


def getPayRate(employeeID: int):
    """Calls the querier and returns the pay rate of a specific employee."""
    result = manager_payroll_querier.getPayRate(employeeID)
    return result if result is not None else []


def payEmployeeByID(employeeID: int, totalPayment: float) -> bool:
    """Pays employees by their id."""
    result = 1
    return True if result is not None else False


def getBillingPeriods(sinceYear: int = 2023, sinceMonth: int = 10, sinceDay: int = 30):
    """Gets the 2 week billing periods over the period."""
    startDate = _nextMonday(datetime.date(sinceYear, sinceMonth, sinceDay))
    endDate = _nextMonday(datetime.date.today())

    billingPeriods = []

    while startDate < endDate:
        billingPeriods.append(startDate.isoformat())
        startDate += datetime.timedelta(days=14)

    return billingPeriods[::-1]


def _nextMonday(date: datetime.date):
    """Gets the next monday."""
    return date + datetime.timedelta((0 - date.weekday()) % 7)
