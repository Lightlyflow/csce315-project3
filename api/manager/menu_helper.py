from api.db import manager_querier


def getMenuItems():
    return manager_querier.getMenuItems()


def getIngredients(itemId: int):
    return manager_querier.getIngredients(itemId)


def addMenuItem(name: str, price: float, inStock: bool, category: str, calories: int):
    manager_querier.addMenuItem(name, price, inStock, category, calories)


def delMenuItem(itemID: int):
    manager_querier.deleteMenuItem(itemID)


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int):
    manager_querier.updateMenuItem(price, inStock, name, category, calories, itemID)


def addIngredient(menuItemID: int, inventoryID: int, quantity: float):
    # TODO :: check if exists
    pass


def delIngredient(uniqueID: int):
    manager_querier.deleteIngredient(uniqueID)


def updateIngredient(quantity: float, ingredientID: int):
    manager_querier.updateIngredient(quantity, ingredientID)

