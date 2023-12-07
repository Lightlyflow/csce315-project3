import datetime

from api.db import employee_querier


def clockInHelper(employeeID: int, activity: str):
    """
    Clock in, rounding to the nearest quarter-hour
    :param employeeID: employee ID
    :param activity: activity name
    :return: None
    """
    employee_querier.clockIn(employeeID, activity)


def clockOutHelper(employeeID: int):
    """
    Clock out, rounding to the nearest quarter-hour
    :param employeeID: employee ID
    :return: None
    """
    employee_querier.clockOut(employeeID)


def getWeek(employeeID, billingPeriod):
    """
    Returns a week of activity for a specific employee based on their ID.
    :param employeeID: employee ID
    :param billingPeriod: start date
    :return: List containing clock in/out entries or [] if nothing found
    """
    result = employee_querier.getWeek(employeeID, billingPeriod)
    return result if result is not None else []


def getBillingPeriods(sinceYear: int = 2023, sinceMonth: int = 10, sinceDay: int = 30):
    """
    Retrieves billing periods (2 weeks in length) from start date to present date.
    :param sinceYear: start year
    :param sinceMonth: start month
    :param sinceDay: start day
    :return: List of billing periods sorted latest first
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
    Computes the date of the next Monday.
    :param date: date
    :return: date object containing next Monday
    """
    return date + datetime.timedelta((0 - date.weekday()) % 7)
