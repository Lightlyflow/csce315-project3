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
