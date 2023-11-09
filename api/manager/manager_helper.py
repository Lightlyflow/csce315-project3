from api.db import manager_querier


def getInventory():
    result = manager_querier.getInventory()
    return result if result is not None else []


def getLowStock():
    result = manager_querier.getLowStock()
    return result if result is not None else []


def orderItems(amount: float, items: [str]):
    for item in items:
        manager_querier.orderItem(amount, item)

