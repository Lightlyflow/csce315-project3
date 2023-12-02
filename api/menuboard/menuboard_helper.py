from api.db import menuboard_querier

def getMenuData():
    return menuboard_querier.getMenuItems()

def getMenuCategories() -> list():

    results = menuboard_querier.getCategoryNames()
    categoryNames = []
    for cat in results:
        categoryNames.append(cat[0])
    return categoryNames

def getToppingNames() -> list():
    results = menuboard_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames