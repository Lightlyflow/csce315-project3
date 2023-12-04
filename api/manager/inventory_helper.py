from api.db import manager_querier


def getInventory():
    result = manager_querier.getInventory()
    return result if result is not None else []


def addInventoryItem(name: str, quantity: float, restockThreshold: float):
    manager_querier.addItemInventory(name, quantity, restockThreshold)


def updateInventoryItem(inventoryID: int, name: str, quantity: float, restockThreshold: float):
    manager_querier.updateItemByID(inventoryID, name, quantity, restockThreshold)


def deleteInventoryItem(inventoryID: int):
    manager_querier.deleteItemByID(inventoryID)


def getLowStock():
    result = manager_querier.getLowStock()
    return result if result is not None else []


def orderItems(amount: float, names: [str]):
    for name in names:
        manager_querier.orderItem(amount, name)


def orderAllItems(amount: float):
    manager_querier.orderAllItems(amount)


def updateThresholds(names: [str], amount):
    for name in names:
        updateThreshold(name, amount)


def updateThreshold(name: str, amount: float):
    manager_querier.updateThreshold(name, amount)
