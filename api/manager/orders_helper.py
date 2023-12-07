from time import struct_time, strftime, strptime
from api.db import manager_querier


def getOrders(startDate: str, endDate: str):
    """
    Gets orders from range [startDate, endDate)
    :param startDate: date, inclusive
    :param endDate: date, non-inclusive
    :return: List containing orders
    """
    result = manager_querier.getOrders(startDate, endDate)
    return result if result is not None else []


def getOrderItems(orderID: int):
    """
    Calls the querier and gets orders by order id.
    :param orderID: order ID
    :return: List containing order items
    """
    result = manager_querier.getOrderItemsByOrderID(orderID)
    return result if result is not None else []


# def convertDate(date: str) -> str:
#     """Converts from MM/DD/YYYY to YYYY-MM-DD"""
#     convertedDate: struct_time = strptime(date, "%m/%d/%Y")
#     convertedDate: str = strftime("%Y-%m-%d", convertedDate)
#     return convertedDate


def deleteOrder(orderID: int):
    """
    Calls the querier and deletes orders by order id.
    :param orderID: order ID
    :return: None
    """
    manager_querier.deleteOrder(orderID)
    manager_querier.deleteOrderParts(orderID)
