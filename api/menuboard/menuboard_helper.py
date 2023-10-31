from api.db import menuboard_querier

def getMenuData():
    return menuboard_querier.getMenuItems()

def getMenuCategories(menuQuery) -> list():
    results = menuQuery
    categories = set()
    for result in results:
        categories.add(result[1])
    return list(categories)


def getToppingNames() -> list():
    results = menuboard_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames