import datetime

from api.db import manager_payroll_querier


def getTimesheet():
    """
    Calls the querier and returns the timesheet from the database.
    :return: List containing timesheet entries
    """
    result = manager_payroll_querier.getTimesheet()
    return result if result is not None else []


def getTimesheetByID(employeeID: int, billingPeriod: str):
    """
    Calls the querier and returns the timesheet for employee over a period from the database.
    :param employeeID: employee ID
    :param billingPeriod: start date
    :return: List containing timesheet entries
    """
    result = manager_payroll_querier.getTimesheetByID(employeeID, billingPeriod)
    return result if result is not None else []


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    """
    Calls the querier and adds a timesheet entry to the database.
    :param employeeID: employee ID
    :param activity: new activity
    :param clockIn: new clock in time
    :param clockOut: new clock out time
    :return: None
    """
    manager_payroll_querier.addTimesheetEntry(employeeID, activity, clockIn, clockOut)


def updateTimesheetEntry(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    """
    Calls the querier and updates a timesheet entry in the database.
    :param entryID: entry ID
    :param employeeID: new employee ID
    :param activity: new activity name
    :param clockIn: new clock in time
    :param clockOut: new clock out time
    :return: None
    """
    manager_payroll_querier.updateTimesheetEntryByID(entryID, employeeID, activity, clockIn, clockOut)


def deleteTimesheetEntry(entryID: int):
    """
    Calls the querier and deletes a timesheet entry from the database.
    :param entryID: entry ID
    :return: None
    """
    manager_payroll_querier.deleteTimesheetEntry(entryID)


def getEmployees():
    """
    Calls the querier and returns the employees on payroll from the database.
    :return: List of employees
    """
    result = manager_payroll_querier.getEmployees()
    return result if result is not None else []


def getTotalHours(employeeID: int, billingPeriod: str):
    """
    Calls the querier and returns the total hours for an employee over 2 weeks from the database.
    :param employeeID: employee ID
    :param billingPeriod: start date
    :return: List containing total hours
    """
    result = manager_payroll_querier.getTotalHours(employeeID, billingPeriod)
    return result if result is not None else []


def getPayRate(employeeID: int):
    """
    Calls the querier and returns the pay rate of a specific employee.
    :param employeeID: employee ID
    :return: List containing pay rate
    """
    result = manager_payroll_querier.getPayRate(employeeID)
    return result if result is not None else []


def payEmployeeByID(employeeID: int, totalPayment: float) -> bool:
    """
    Pays employees by their id. Add whatever payment service here!
    :param employeeID: employee ID
    :param totalPayment: total payment (this is calculated by the client lol)
    :return: True if paid or False otherwise
    """
    result = 1
    return True if result is not None else False


def getBillingPeriods(sinceYear: int = 2023, sinceMonth: int = 10, sinceDay: int = 30):
    """
    Gets the 2 week billing periods since given arguments.
    :param sinceYear: start year
    :param sinceMonth: start month
    :param sinceDay: start day
    :return: List of dates
    """
    startDate = _nextMonday(datetime.date(sinceYear, sinceMonth, sinceDay))
    endDate = _nextMonday(datetime.date.today())

    billingPeriods = []

    while startDate < endDate:
        billingPeriods.append(startDate.isoformat())
        startDate += datetime.timedelta(days=14)

    return billingPeriods[::-1]


def _nextMonday(date: datetime.date):
    """
    Gets the next monday.
    :param date: any date
    :return: next Monday in date object
    """
    return date + datetime.timedelta((0 - date.weekday()) % 7)
