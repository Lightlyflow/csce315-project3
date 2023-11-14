from api.db import manager_querier


def getMenuItems():
    return manager_querier.getMenuItems()


def getIngredients(itemId: int):
    return manager_querier.getIngredients(itemId)
