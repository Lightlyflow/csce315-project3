import datetime

from api.db import employee_querier


def clockInHelper(employeeID: int, activity: str):
    """Clock in, rounding to the nearest quarter-hour"""
    employee_querier.clockIn(employeeID, activity)


def clockOutHelper(employeeID: int):
    """Clock out, rounding to the nearest quarter-hour"""
    employee_querier.clockOut(employeeID)


def getWeek(employeeID, billingPeriod):
    """Returns a week of activity for a specific employee based on their ID."""
    result = employee_querier.getWeek(employeeID, billingPeriod)
    return result if result is not None else []


def getBillingPeriods(sinceYear: int = 2023, sinceMonth: int = 10, sinceDay: int = 30):
    """Retrieves billing periods from start date to present date."""
    startDate = _nextMonday(datetime.date(sinceYear, sinceMonth, sinceDay))
    endDate = _nextMonday(datetime.date.today())

    billingPeriods = []

    while startDate < endDate:
        billingPeriods.append(startDate.isoformat())
        startDate += datetime.timedelta(days=14)

    return billingPeriods[::-1]


def _nextMonday(date: datetime.date):
    """Computes the date of the next Monday."""
    return date + datetime.timedelta((0 - date.weekday()) % 7)
