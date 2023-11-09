from .querier import execute


def getInventory():
    return execute("SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table;")


def getLowStock():
    return execute("SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table WHERE quantity<restockThreshold;")


def orderItem(amount: float, item: str):
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount} WHERE name='{item}';")

