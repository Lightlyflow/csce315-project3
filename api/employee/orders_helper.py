from datetime import datetime

from api.db import employee_querier


def getOrders():
    """Gets orders from range [startDate, endDate)"""
    startDate = datetime.today().strftime('%Y-%m-%d')
    result = employee_querier.getOrders(startDate)
    return result if result is not None else []


def getOrderItems(orderID: int):
    result = employee_querier.getOrderItemsByOrderID(orderID)
    return result if result is not None else []


def markOrder(orderID: int, status: str):
    employee_querier.markOrder(orderID, status)
