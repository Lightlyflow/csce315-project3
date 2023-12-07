from datetime import datetime

from api.db import employee_querier, manager_querier


def getOrders():
    """
    Gets unfulfilled orders for today
    :return: orders from range [startDate, endDate)
    """
    startDate = datetime.today().strftime('%Y-%m-%d')
    result = employee_querier.getOrders(startDate)
    return result if result is not None else []


def getOrderItems(orderID: int):
    """
    Gets items comprising an order
    :param orderID: order ID
    :return: List containing order items or [] if nothing found
    """
    result = employee_querier.getOrderItemsByOrderID(orderID)
    return result if result is not None else []


def markOrder(orderID: int, status: str):
    """
    Marks an order with a status
    :param orderID: order ID
    :param status: new status
    :return: None
    """
    employee_querier.markOrder(orderID, status)


def deleteOrder(orderID: int):
    """
    Deletes an order and its corresponding items
    :param orderID: order ID
    :return: None
    """
    manager_querier.deleteOrder(orderID)
    manager_querier.deleteOrderParts(orderID)
