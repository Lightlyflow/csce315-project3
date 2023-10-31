from api.db import manager_querier


def getInventory():
    return manager_querier.getInventory()
