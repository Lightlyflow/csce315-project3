from .querier import execute


def getTimesheet():
    return execute(f"SELECT id, employeeid, activity, clockin, clockout FROM clockinout;")


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    execute(f"INSERT INTO clockinout (employeeid, clockin, clockout, activity) VALUES ({employeeID}, '{clockIn}', '{clockOut}', '{activity}');")


def updateTimesheetEntryByID(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    execute(f"UPDATE clockinout SET employeeID={employeeID}, activity='{activity}', clockIn=round_time_quarter_hour('{clockIn}'), clockOut=round_time_quarter_hour('{clockOut}') WHERE id={entryID};")


def deleteTimesheetEntry(entryID: int):
    execute(f"DELETE FROM clockinout WHERE id={entryID};")
