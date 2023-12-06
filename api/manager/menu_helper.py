from api.db import manager_querier


def getMenuItems():
    """Calls the querier and returns the menu items from the database."""
    return manager_querier.getMenuItems()


def getIngredients(itemId: int):
    """Calls the querier and returns the item ingredients from the database."""
    return manager_querier.getIngredients(itemId)


def addMenuItem(name: str, price: float, inStock: bool, category: str, calories: int, imageID: int):
    """Calls the querier and adds a menu item to the database."""
    if imageID < 0:
        imageID = "NULL"
    manager_querier.addMenuItem(name, price, inStock, category, calories, imageID)


def delMenuItem(itemID: int):
    """Calls the querier and deletes a menu item from the database."""
    manager_querier.deleteMenuItem(itemID)


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int, imageID: int):
    """Calls the querier and updates a menu item in the database."""
    if imageID < 0:
        imageID = "NULL"
    manager_querier.updateMenuItem(price, inStock, name, category, calories, itemID, imageID)


def addIngredient(menuItemID: int, name: str, quantity: float):
    """Calls the querier and adds a menu item ingredient to the database."""
    result = manager_querier.getIngredientInventoryID(name)
    if len(result) > 0:
        inventoryID = result[0][0]
    else:
        manager_querier.createIngredient(name)
        inventoryID = manager_querier.getIngredientInventoryID(name)[0][0]

    manager_querier.addIngredient(menuItemID, inventoryID, quantity)


def delIngredient(uniqueID: int):
    """Calls the querier and deletes a menu item ingredient from the database."""
    manager_querier.deleteIngredient(uniqueID)


def updateIngredient(quantity: float, ingredientID: int):
    """Calls the querier and updates a menu item ingredient in the database."""
    manager_querier.updateIngredient(quantity, ingredientID)


def getMenuCategories():
    """Calls the querier and returns the menu item categories from the database."""
    result = manager_querier.getMenuItemCategories()
    for i, row in enumerate(result):
        row.insert(0, i + 1)
    return result if not None else []


def addMenuCategories(categories: [str]):
    """Calls the querier and adds a menu item category to the database."""
    cats: [str] = []
    for cat in categories:
        cats.append(f"('{cat}', -1)")

    manager_querier.addCategories(", ".join(cats))


def updateMenuCategoriesOrder(categories: [str]):
    """Calls the querier and updates the order of the menu item categories in the database."""
    cats: [str] = []
    for cat in categories:
        cats.append(f"('{cat[1]}', {cat[0]})")

    manager_querier.updateCategories(", ".join(cats))
    manager_querier.removeUnusedCategories()
