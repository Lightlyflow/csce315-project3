from api.db import manager_querier


def getMenuItems():
    """
    Calls the querier and returns the menu items from the database.
    :return: List of menu items
    """
    return manager_querier.getMenuItems()


def getIngredients(itemId: int):
    """
    Calls the querier and returns the item ingredients from the database.
    :param itemId: item ID
    :return: List of ingredients
    """
    return manager_querier.getIngredients(itemId)


def addMenuItem(name: str, price: float, inStock: bool, category: str, calories: int, imageID: int):
    """
    Calls the querier and adds a menu item to the database.
    :param name: new name
    :param price: new price
    :param inStock: new stock status
    :param category: new category
    :param calories: new calorie count
    :param imageID: new image ID
    :return: None
    """
    if imageID < 0:
        imageID = "NULL"
    manager_querier.addMenuItem(name, price, inStock, category, calories, imageID)


def delMenuItem(itemID: int):
    """
    Calls the querier and deletes a menu item from the database.
    :param itemID: item ID
    :return: None
    """
    manager_querier.deleteMenuItem(itemID)


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int, imageID: int):
    """
    Calls the querier and updates a menu item in the database.
    :param price: new price
    :param inStock: new stock status
    :param name: new name
    :param category: new category
    :param calories: new calorie count
    :param itemID: item ID
    :param imageID: new image ID
    :return: None
    """
    if imageID < 0:
        imageID = "NULL"
    manager_querier.updateMenuItem(price, inStock, name, category, calories, itemID, imageID)


def addIngredient(menuItemID: int, name: str, quantity: float):
    """
    Calls the querier and adds a menu item ingredient to the database.
    Will create a new inventory item if it doesn't already exist.
    :param menuItemID: menu item ID
    :param name: new name
    :param quantity: new quantity
    :return: None
    """
    result = manager_querier.getIngredientInventoryID(name)
    if len(result) > 0:
        inventoryID = result[0][0]
    else:
        manager_querier.createIngredient(name)
        inventoryID = manager_querier.getIngredientInventoryID(name)[0][0]

    manager_querier.addIngredient(menuItemID, inventoryID, quantity)


def delIngredient(uniqueID: int):
    """
    Calls the querier and deletes a menu item ingredient from the database.
    :param uniqueID: ingredient ID
    :return: None
    """
    manager_querier.deleteIngredient(uniqueID)


def updateIngredient(quantity: float, ingredientID: int):
    """
    Calls the querier and updates a menu item ingredient in the database.
    :param quantity: new quantity
    :param ingredientID: ingredient ID
    :return: None
    """
    manager_querier.updateIngredient(quantity, ingredientID)


def getMenuCategories():
    """
    Calls the querier and returns the menu item categories from the database.
    :return: List of categories with their priorities (as they appear to the end user)
    """
    result = manager_querier.getMenuItemCategories()
    for i, row in enumerate(result):
        row.insert(0, i + 1)
    return result if not None else []


def addMenuCategories(categories: [str]):
    """
    Calls the querier and adds menu item categories to the database.
    :param categories: list of categories
    :return: None
    """
    cats: [str] = []
    for cat in categories:
        cats.append(f"('{cat}', -1)")

    manager_querier.addCategories(", ".join(cats))


def updateMenuCategoriesOrder(categories: [str]):
    """
    Calls the querier and updates the order of the menu item categories in the database.
    :param categories: list of categories
    :return: None
    """
    cats: [str] = []
    for cat in categories:
        cats.append(f"('{cat[1]}', {cat[0]})")

    manager_querier.updateCategories(", ".join(cats))
    manager_querier.removeUnusedCategories()
