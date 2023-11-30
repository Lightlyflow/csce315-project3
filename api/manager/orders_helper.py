from time import struct_time, strftime, strptime
from api.db import manager_querier


def getOrders(startDate: str, endDate: str):
    """Gets orders from range [startDate, endDate)"""
    startDate = convertDate(startDate)
    endDate = convertDate(endDate)

    result = manager_querier.getOrders(startDate, endDate)
    return result if result is not None else []


def convertDate(date: str) -> str:
    """Converts from MM/DD/YYYY to YYYY-MM-DD"""
    convertedDate: struct_time = strptime(date, "%m/%d/%Y")
    convertedDate: str = strftime("%Y-%m-%d", convertedDate)
    return convertedDate
