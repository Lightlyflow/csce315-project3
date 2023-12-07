if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv

    load_dotenv()
else:
    from .querier import execute


def getMenuItems():
    """
    Retrieve all menu items from the database.
    :return: List containing name, category, price, calories, image url (or -1 if it doesn't exist)
    """
    return execute(
        f"SELECT m.name, m.category, m.price, m.calories, COALESCE(i.url, '-1') FROM menu_items_table m JOIN category_priority p ON m.category = p.name LEFT JOIN images i ON m.imageid=i.id ORDER BY p.priority;")


def getMenuCategories():
    """
    Retrieve all menu categories from the database.
    :return: List of menu category names, ordered by highest priority
    """
    return execute(f"SELECT name FROM category_priority order by priority;")


if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv

    load_dotenv()

else:
    from .querier import execute


def getToppingNames():
    """
    Retrieve topping names from the database.
    :return: List containing name and price for each topping
    """
    return execute(f"SELECT name, price from topping_table;")


def getMenuItemId(name):
    """
    Return a menu item ID based on its name.
    :param name: menu item name
    :return: List containing menu item ID
    """
    return execute(f"SELECT menuitemid FROM menu_items_table WHERE name='{name}';")


def getMenuItemComponents(menuItemId):
    """
    Return ingredients of a menu item based on its ID.
    :param menuItemId: menu item ID
    :return: List containing inventory ID and quantity for each ingredient
    """
    return execute(f"SELECT inventoryid, quantity FROM menu_part_table WHERE menuitemid={menuItemId};")


def getIngredientQuantityInventory(inventoryId):
    """
    Return quantity of a specific inventory item based on its ID.
    :param inventoryId: ingredient inventory ID
    :return: List containing quantity of ingredient
    """
    return execute(f"SELECT quantity FROM inventory_table WHERE inventoryid={inventoryId};")


def getToppingId(name):
    """
    Return an inventory ID based on its name.
    :param name: topping name
    :return: List containing inventory ID
    """
    return execute(f"SELECT inventoryid FROM inventory_table WHERE name='{name}';")


def setIngredientQuantityInventory(inventoryId, quantity):
    """
    Set the quantity of an inventory item based on its ID.
    :param inventoryId: inventory ID
    :param quantity: new quantity
    :return: None
    """
    return execute(f"UPDATE inventory_table SET quantity={quantity} WHERE inventoryid={inventoryId};")


def subtractIngredientQuantityInventory(inventoryId, quantity):
    """
    Subtract an ingredient quantity from inventory based on its ID.
    :param inventoryId: inventory ID
    :param quantity: amount to reduce by
    :return: None
    """
    return execute(f"UPDATE inventory_table SET quantity = quantity - {quantity} WHERE inventoryid={inventoryId};")


def getMaxOrderId():
    """
    Retrieves the most recent order ID from the database.
    :return: Maximum order ID
    """
    return execute(f"SELECT max(orderid) FROM order_table;")


def getMaxUniqueId():
    """
    Retrieves the most recently ordered item from the database.
    :return: Maximum order part ID
    """
    return execute(f"SELECT max(uniqueid) FROM order_part_table;")


def insertIntoOrderPartTable(uniqueId, orderId, menuItemId, topping1, topping2, topping3, price, sweetness, ice):
    """
    Inserts a customer's order item (most likely one of many) into the database.
    :param uniqueId: new unique ID
    :param orderId: new order ID
    :param menuItemId: new menu item ID
    :param topping1: new topping ID
    :param topping2: new topping ID
    :param topping3: new topping ID
    :param price: total price
    :param sweetness: sweetness level
    :param ice: ice level
    :return: None
    """
    return execute(
        f"INSERT INTO order_part_table (uniqueid, orderid, menuitemid, toppingid1, toppingid2, toppingid3, price, sweetness, ice) VALUES ({uniqueId}, {orderId}, {menuItemId}, {topping1}, {topping2}, {topping3}, {price}, {sweetness}, {ice});")


def insertIntoOrderTable(orderId, price, email, dateString):
    """
    Inserts an entire customer order (with pending status) into the database.
    :param orderId: new order ID
    :param price: total price
    :param email: customer email
    :param dateString: date to fulfill order by
    :return: None
    """
    return execute(
        f"INSERT INTO order_table (orderid, employeeid, dateordered, price, email, status) VALUES ({orderId}, -1, '{dateString}', {price}, '{email}', 'pending');")


def insertIntoOrderTableCurrent(orderId, price, email, employeeId):
    """
    Inserts an entire customer order into the database with the time of the order stored as the current time.
    :param orderId: new order ID
    :param price: new total price
    :param email: new customer email
    :param employeeId: new employee ID
    :return: None
    """
    return execute(
        f"INSERT INTO order_table (orderid, employeeid, dateordered, price, email, status) VALUES ({orderId}, {employeeId}, (NOW() AT TIME ZONE 'America/Chicago'), {price}, '{email}', 'pending');")


def getMenuItemPrice(menuItemId):
    """
    Return menu item's price based on its ID.
    :param menuItemId: menu item ID
    :return: List containing price of menu item
    """
    return execute(f"SELECT price FROM menu_items_table WHERE menuitemid = {menuItemId};")


def getToppingPrice(toppingId):
    """
    Return a topping's price based on its ID.
    :param toppingId: topping ID
    :return: List containing topping price
    """
    return execute(f"SELECT price FROM topping_table WHERE inventoryid = {toppingId};")


def getOrderInfoForUser(email):
    """
    Retrieves all orders for a specific user organized by date (including dates in the future).
    :param email: customer email
    :return: List containing order ID, date ordered, total price, menu item name, toppings, etc.
    """
    return execute(
        f"SELECT ot.orderid, ot.dateordered, ot.price AS order_price, mi.name AS menu_item_name, t1.name AS topping1_name, t2.name AS topping2_name, t3.name AS topping3_name, opt.price, opt.sweetness, opt.ice FROM order_table ot JOIN order_part_table opt ON ot.orderid = opt.orderid LEFT JOIN topping_table t1 ON opt.toppingid1 = t1.toppingid LEFT JOIN topping_table t2 ON opt.toppingid2 = t2.toppingid LEFT JOIN topping_table t3 ON opt.toppingid3 = t3.toppingid JOIN menu_items_table mi ON opt.menuitemid = mi.menuitemid WHERE ot.email = '{email}' ORDER BY ot.dateordered DESC;")
