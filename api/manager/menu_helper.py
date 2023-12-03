from api.db import manager_querier


def getMenuItems():
    return manager_querier.getMenuItems()


def getIngredients(itemId: int):
    return manager_querier.getIngredients(itemId)


def addMenuItem(name: str, price: float, inStock: bool, category: str, calories: int):
    manager_querier.addMenuItem(name, price, inStock, category, calories)


def delMenuItem(itemID: int):
    # TODO :: Remove associated menu item parts (ingredients)
    manager_querier.deleteMenuItem(itemID)


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int):
    manager_querier.updateMenuItem(price, inStock, name, category, calories, itemID)


def addIngredient(menuItemID: int, name: str, quantity: float):
    # TODO :: Check if already exists in db!
    result = manager_querier.getIngredientInventoryID(name)
    if len(result) > 0:
        inventoryID = result[0][0]
    else:
        manager_querier.createIngredient(name)
        inventoryID = manager_querier.getIngredientInventoryID(name)[0][0]

    manager_querier.addIngredient(menuItemID, inventoryID, quantity)


def delIngredient(uniqueID: int):
    manager_querier.deleteIngredient(uniqueID)


def updateIngredient(quantity: float, ingredientID: int):
    manager_querier.updateIngredient(quantity, ingredientID)


def getMenuCategories():
    result = manager_querier.getMenuItemCategories()
    for i, row in enumerate(result):
        row.insert(0, i + 1)
    return result if not None else []


def addMenuCategories(categories: [str]):
    cats: [str] = []
    for cat in categories:
        cats.append(f"('{cat}', -1)")

    manager_querier.addCategories(", ".join(cats))


def updateMenuCategoriesOrder(categories: [str]):
    cats: [str] = []
    for cat in categories:
        cats.append(f"('{cat[1]}', {cat[0]})")

    manager_querier.updateCategories(", ".join(cats))
    manager_querier.removeUnusedCategories()
