from .querier import execute


def getTimesheet():
    """Retrieves a table of all employee activity from the database."""
    return execute(
        f"SELECT id, employeeid, activity, clockin, clockout, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours FROM clockinout;")


def getTimesheetByID(employeeID: int, billingPeriod: str):
    """Retrieves activity for a specific employee and billing period based on their ID."""
    return execute(
        f"SELECT id, employeeid, activity, clockin, clockout, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours FROM clockinout"
        f" WHERE employeeid={employeeID}"
        f" AND (clockout >= '{billingPeriod}' AND clockout <= (to_timestamp('{billingPeriod}', 'YYYY-MM-DD') + INTERVAL '14 day'));")


def addTimesheetEntry(employeeID: int, activity: str, clockIn: str, clockOut: str):
    """Inserts an employee shift into the time sheet."""
    execute(
        f"INSERT INTO clockinout (employeeid, clockin, clockout, activity) VALUES ({employeeID}, '{clockIn}', '{clockOut}', '{activity}');")


def updateTimesheetEntryByID(entryID: int, employeeID: int, activity: str, clockIn: str, clockOut: str):
    """Updates the information of an employee shift based on their ID."""
    execute(
        f"UPDATE clockinout SET employeeID={employeeID}, activity='{activity}', clockIn=round_time_quarter_hour('{clockIn}'), clockOut=round_time_quarter_hour('{clockOut}') WHERE id={entryID};")


def deleteTimesheetEntry(entryID: int):
    """Deletes an entry from the time sheet by ID."""
    execute(f"DELETE FROM clockinout WHERE id={entryID};")


def getPayRate(employeeID: int):
    """Returns the pay rate for a specific employee based on their ID."""
    return execute(f"SELECT pay_rate from employee_table WHERE employeeid={employeeID};")


def getEmployees():
    """Retrieves all employee names and their associated IDs from the database."""
    return execute(f"SELECT employeeID, name FROM employee_table ORDER BY name;")


def getTotalHours(employeeID: int, billingPeriod: str):
    """Returns an employee's total hours worked over a specific billing period based on their ID."""
    return execute(f"SELECT SUM(EXTRACT(EPOCH FROM clockout -  clockin)/3600) AS hours"
                   f" FROM clockinout"
                   f" WHERE employeeid = {employeeID}"
                   f" AND (clockout >= '{billingPeriod}'"
                   f" AND clockout <= (to_timestamp('{billingPeriod}', 'YYYY-MM-DD') + INTERVAL '14 day'));")
