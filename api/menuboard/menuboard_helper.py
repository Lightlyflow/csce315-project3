from api.db import menuboard_querier

def getMenuData():
    """Returns all menu items from the database."""
    return menuboard_querier.getMenuItems()

def getMenuCategories() -> list():
    """Returns all menu category names from the database in order of priority."""
    results = menuboard_querier.getCategoryNames()
    categoryNames = []
    for cat in results:
        categoryNames.append(cat[0])
    return categoryNames

def getToppingNames() -> list():
    """Returns all topping names from the database."""
    results = menuboard_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames