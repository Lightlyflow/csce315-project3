from api.db import menuboard_querier

def getMenuData():
    return menuboard_querier.getMenuItems()

def getMenuCategories():
    results = menuboard_querier.getMenuCategories()
    categories = [item for sublist in results for item in sublist]
    return categories


def getToppingNames() -> list():
    results = menuboard_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames