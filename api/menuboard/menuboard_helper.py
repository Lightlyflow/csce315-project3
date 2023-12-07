from api.db import menuboard_querier


def getMenuData():
    """
    Returns all in stock menu items from the database.
    :return: List of menu items
    """
    return menuboard_querier.getMenuItems()


def getMenuCategories() -> []:
    """
    Returns all menu category names from the database in order of priority.
    :return: Flattened list of category names
    """
    results = menuboard_querier.getCategoryNames()
    categoryNames = []
    for cat in results:
        categoryNames.append(cat[0])
    return categoryNames


def getToppingNames() -> []:
    """
    Returns all topping names from the database.
    :return: Flattened list of topping names
    """
    results = menuboard_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames
