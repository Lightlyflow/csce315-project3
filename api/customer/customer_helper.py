from api.db import customer_querier

def getMenuCategories() -> list():
    results = customer_querier.getMenuItems()
    categories = set()
    for result in results:
        categories.add(result[1])
    return list(categories)

def getMenuItems(category) ->list():
    categories = customer_querier.getMenuItems()
    menuItems = []
    for cat in categories:
        if category == cat[1]:
            menuItems.append(cat[0])
    return menuItems