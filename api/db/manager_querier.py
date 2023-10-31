from .querier import execute


def getInventory():
    return execute("SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table;")
