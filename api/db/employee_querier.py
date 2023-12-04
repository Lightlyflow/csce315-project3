from .querier import execute


def clockIn(employeeID: int, activity: str):
    """Creates new row with activity and start time for employee. Time is rounded to nearest 15 minutes"""
    execute(f"INSERT INTO clockinout (employeeID, activity, clockin) VALUES ({employeeID}, '{activity}', round_time_quarter_hour(NOW()))")


def clockOut(employeeID: int):
    """Updates latest clockin row with clock out time. Time is rounded to nearest 15 minutes"""
    execute(f"UPDATE clockinout SET clockout=round_time_quarter_hour(NOW())"
            f"WHERE employeeid={employeeID} "
            f"AND clockout=(SELECT MAX(clockin) FROM clockinout "
            f"              WHERE employeeid={employeeID});")
    
def getWeek1(employeeID, lastWeekDate, currDate):
    return execute(f"""SELECT employeeid, clockin, clockout, activity, EXTRACT(EPOCH FROM clockout -  clockin) AS hours
        FROM clockinout
        WHERE employeeid = {employeeID} AND (clockin >= '{lastWeekDate}' AND clockin <= '{currDate}');""")

def getWeek2(employeeID, secondLastWeekDate, lastWeekDate):
    return execute(f"""SELECT employeeid, clockin, clockout, activity, EXTRACT(EPOCH FROM clockout -  clockin) AS hours
        FROM clockinout
        WHERE employeeid = {employeeID} AND (clockin >= '{secondLastWeekDate}' AND clockin <= '{lastWeekDate}');""")