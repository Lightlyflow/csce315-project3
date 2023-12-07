from api.db import manager_querier


def getInventory():
    """
    Calls the querier and returns the inventory from the database.
    :return: List of inventory items or [] if not found
    """
    result = manager_querier.getInventory()
    return result if result is not None else []


def addInventoryItem(name: str, quantity: float, restockThreshold: float):
    """
    Calls the querier and adds an inventory item to the database.
    :param name: new name
    :param quantity: new quantity
    :param restockThreshold: new restock threshold
    :return: None
    """
    manager_querier.addItemInventory(name, quantity, restockThreshold)


def updateInventoryItem(inventoryID: int, name: str, quantity: float, restockThreshold: float):
    """
    Calls the querier and updates an inventory item in the database.
    :param inventoryID: inventory ID
    :param name: new name
    :param quantity: new quantity
    :param restockThreshold: new restock threshold
    :return: None
    """
    manager_querier.updateItemByID(inventoryID, name, quantity, restockThreshold)


def deleteInventoryItem(inventoryID: int):
    """
    Calls the querier and deletes an inventory item in the database.
    :param inventoryID: inventory ID
    :return: None
    """
    manager_querier.deleteItemByID(inventoryID)


def getLowStock():
    """
    Calls the querier and returns the items with low stock in the database.
    :return: List of low stock items or [] if not found
    """
    result = manager_querier.getLowStock()
    return result if result is not None else []


def orderItems(amount: float, names: [str]):
    """
    Calls the querier and updates the items' inventory quantities in the database.
    :param amount: amount to add
    :param names: list of names
    :return: None
    """
    for name in names:
        manager_querier.orderItem(amount, name)


def orderAllItems(amount: float):
    """
    Calls the querier and updates all inventory items quantities in the database.
    :param amount: amount
    :return: None
    """
    manager_querier.orderAllItems(amount)


def updateThresholds(names: [str], amount):
    """
    Updates the thresholds of inventory items.
    :param names: list of inventory names
    :param amount: new threshold
    :return: None
    """
    for name in names:
        updateThreshold(name, amount)


def updateThreshold(name: str, amount: float):
    """
    Calls the querier and updates the thresholds of items in the database.
    :param name: name of inventory item
    :param amount: new threshold
    :return: None
    """
    manager_querier.updateThreshold(name, amount)
