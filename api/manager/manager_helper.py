from api.db import manager_querier


def getInventory():
    result = manager_querier.getInventory()
    return result if result is not None else []


def getLowStock():
    result = manager_querier.getLowStock()
    return result if result is not None else []
