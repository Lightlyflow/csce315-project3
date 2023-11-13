if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv
    load_dotenv()

else:
    from .querier import execute


def getMenuItems():
    return execute(f"SELECT name, category, price FROM menu_items_table;")

if __name__ == '__main__':
    # If you want to run this, delete the period in front of the import statements in this file
    # but make sure to add them back
    res = getUserByEmail("test@gmail.com")
    print(res)
if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv
    load_dotenv()

else:
    from .querier import execute



def getToppingNames():
    return execute(f"Select name from topping_table;")

def getMenuItemId(name):
    return execute(f"SELECT menuitemid FROM menu_items_table WHERE name='{name}';")

def getMenuItemComponents(menuItemId):
    return execute(f"SELECT inventoryid, quantity FROM menu_part_table WHERE menuitemid={menuItemId};")

def getIngredientQuantityInventory(inventoryId):
    return execute(f"SELECT quantity FROM inventory_table WHERE inventoryid={inventoryId};")

def getToppingId(name):
    return execute(f"SELECT inventoryid FROM inventory_table WHERE name='{name}';")

def setIngredientQuantityInventory(inventoryId, quantity):
    return execute(f"UPDATE inventory_table SET quantity={quantity} WHERE inventoryid={inventoryId};")

def getMaxOrderId():
    return execute(f"SELECT max(orderid) FROM order_table;")

def insertIntoOrderTable(orderId, price, email):
    return execute(f"INSERT INTO order_table (orderid, employeeid, dateordered, price, email) VALUES ({orderId}, -1, CURRENT_TIMESTAMP, {price}, {email});")

def getMenuItemPrice(menuItemId):
    return execute(f"SELECT price FROM menu_items_table WHERE menuitemid = {menuItemId};")

def getToppingPrice(toppingId):
    return execute(f"")

if __name__ == '__main__':
    # If you want to run this, delete the period in front of the import statements in this file
    # but make sure to add them back
    res = getUserByEmail("test@gmail.com")
    print(res)