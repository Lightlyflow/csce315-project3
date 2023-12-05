from .querier import execute


def getTimesheet():
    return execute(f"SELECT id, employeeid, activity, clockin, clockout, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours FROM clockinout;")


def getTimesheetByID(employeeID: int, startDate: str, endDate: str):
    return execute(f"SELECT id, employeeid, activity, clockin, clockout, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours FROM clockinout"
                   f" WHERE employeeid={employeeID}"
                   f" AND (clockin >= '{startDate}' AND clockin <= '{endDate}');")


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    execute(f"INSERT INTO clockinout (employeeid, clockin, clockout, activity) VALUES ({employeeID}, '{clockIn}', '{clockOut}', '{activity}');")


def updateTimesheetEntryByID(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    execute(f"UPDATE clockinout SET employeeID={employeeID}, activity='{activity}', clockIn=round_time_quarter_hour('{clockIn}'), clockOut=round_time_quarter_hour('{clockOut}') WHERE id={entryID};")


def deleteTimesheetEntry(entryID: int):
    execute(f"DELETE FROM clockinout WHERE id={entryID};")


def getEmployees():
    return execute(f"SELECT employeeID, name FROM employee_table;")


def getTotalHours(employeeID: int, startDate: str, endDate: str):
    return execute(f"")
