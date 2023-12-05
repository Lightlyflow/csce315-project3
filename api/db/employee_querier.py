from .querier import execute


def clockIn(employeeID: int, activity: str):
    """Creates new row with activity and start time for employee. Time is rounded to nearest 15 minutes"""
    execute(
        f"INSERT INTO clockinout (employeeID, activity, clockin) VALUES ({employeeID}, '{activity}', round_time_quarter_hour(NOW()))")


def clockOut(employeeID: int):
    """Updates latest clockin row with clock out time. Time is rounded to nearest 15 minutes"""
    execute(f"UPDATE clockinout SET clockout=round_time_quarter_hour(NOW())"
            f"WHERE employeeid={employeeID} "
            f"AND clockin=(SELECT MAX(clockin) FROM clockinout "
            f"              WHERE employeeid={employeeID});")


def getWeek(employeeID, startDate, endDate):
    return execute(f"""SELECT employeeid, clockin, clockout, activity, EXTRACT(EPOCH FROM clockout -  clockin)/3600 AS hours
        FROM clockinout
        WHERE employeeid = {employeeID} AND (clockin >= '{startDate}' AND clockin <= '{endDate}');""")
