from api.db import manager_querier


def getInventory():
    result = manager_querier.getInventory()
    return result if result is not None else []


def getLowStock():
    result = manager_querier.getLowStock()
    return result if result is not None else []


def orderItems(amount: float, names: [str]):
    for name in names:
        manager_querier.orderItem(amount, name)


def orderAllItems(amount: float):
    manager_querier.orderAllItems(amount)


def updateThreshold(name: str, amount: float):
    manager_querier.updateThreshold(name, amount)
