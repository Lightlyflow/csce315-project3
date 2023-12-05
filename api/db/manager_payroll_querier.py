from .querier import execute


def getTimesheet():
    return execute(
        f"SELECT id, employeeid, activity, clockin, clockout, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours FROM clockinout;")


def getTimesheetByID(employeeID: int, billingPeriod: str):
    return execute(
        f"SELECT id, employeeid, activity, clockin, clockout, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours FROM clockinout"
        f" WHERE employeeid={employeeID}"
        f" AND (clockout >= '{billingPeriod}' AND clockout <= (to_timestamp('{billingPeriod}', 'YYYY-MM-DD') + INTERVAL '14 day'));")


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    execute(
        f"INSERT INTO clockinout (employeeid, clockin, clockout, activity) VALUES ({employeeID}, '{clockIn}', '{clockOut}', '{activity}');")


def updateTimesheetEntryByID(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    execute(
        f"UPDATE clockinout SET employeeID={employeeID}, activity='{activity}', clockIn=round_time_quarter_hour('{clockIn}'), clockOut=round_time_quarter_hour('{clockOut}') WHERE id={entryID};")


def deleteTimesheetEntry(entryID: int):
    execute(f"DELETE FROM clockinout WHERE id={entryID};")


def getPayRate(employeeID: int):
    return execute(f"SELECT pay_rate from employee_table WHERE employeeid={employeeID};")


def getEmployees():
    return execute(f"SELECT employeeID, name FROM employee_table ORDER BY name;")


def getTotalHours(employeeID: int, billingPeriod: str):
    return execute(f"SELECT SUM(EXTRACT(EPOCH FROM clockout -  clockin)/3600) AS hours"
                   f" FROM clockinout"
                   f" WHERE employeeid = {employeeID}"
                   f" AND (clockout >= '{billingPeriod}'"
                   f" AND clockout <= (to_timestamp('{billingPeriod}', 'YYYY-MM-DD') + INTERVAL '14 day'));")
