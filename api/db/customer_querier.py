if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv
    load_dotenv()

else:
    from .querier import execute


def getMenuItems():
    return execute(f"SELECT name, category, price, calories FROM menu_items_table;")

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
    return execute(f"SELECT name, price from topping_table;")

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

def getMaxUniqueId():
    return execute(f"SELECT max(uniqueid) FROM order_part_table;")

def insertIntoOrderPartTable(uniqueId, orderId, menuItemId, topping1, topping2, topping3, price, sweetness, ice):
    return execute(f"INSERT INTO order_part_table (uniqueid, orderid, menuitemid, toppingid1, toppingid2, toppingid3, price, sweetness, ice) VALUES ({uniqueId}, {orderId}, {menuItemId}, {topping1}, {topping2}, {topping3}, {price}, {sweetness}, {ice});")

def insertIntoOrderTable(orderId, price, email):
    return execute(f"INSERT INTO order_table (orderid, employeeid, dateordered, price, email) VALUES ({orderId}, -1, CURRENT_TIMESTAMP, {price}, '{email}');")

def getMenuItemPrice(menuItemId):
    return execute(f"SELECT price FROM menu_items_table WHERE menuitemid = {menuItemId};")

def getToppingPrice(toppingId):
    return execute(f"SELECT price FROM topping_table WHERE inventoryid = {toppingId};")

if __name__ == '__main__':
    # If you want to run this, delete the period in front of the import statements in this file
    # but make sure to add them back
    res = getUserByEmail("test@gmail.com")
    print(res)