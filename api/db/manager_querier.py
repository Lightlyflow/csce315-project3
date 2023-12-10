from .querier import execute


# ===================== Inventory =====================
def getInventory():
    """
    Retrieves all inventory items from the database.
    :return: List containing inventory ID, name, quantity, and restock threshold
    """
    return execute("SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table;")


def getLowStock():
    """
    Retrieves all inventory items whose stock is lower than their threshold from the database.
    :return: List containing inventory ID, name, quantity, and restock threshold
    """
    return execute(
        "SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table WHERE quantity<restockThreshold;")


def createIngredient(name: str):
    """
    Inserts a new ingredient of quantity 0 into the inventory table.
    :param name: new name
    :return: None
    """
    execute(f"INSERT INTO inventory_table (name, quantity) VALUES ('{name}', 0);")


def orderItem(amount: float, name: str):
    """
    Adds stock to a specific inventory item.
    :param amount: amount to be added
    :param name: name of inventory item
    :return: None
    """
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount} WHERE name='{name}';")


def orderAllItems(amount: float):
    """
    Adds stock to all inventory items.
    :param amount: amount to add
    :return: None
    """
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount};")


def updateThreshold(name: str, amount: float):
    """
    Sets the restock threshold for a specific inventory item.
    :param name: name of inventory item
    :param amount: new amount
    :return: None
    """
    execute(f"UPDATE inventory_table SET restockThreshold={amount} WHERE name='{name}';")


def deleteItemByID(inventoryID: int):
    """
    Deletes an item from the inventory table based on its ID.
    :param inventoryID: inventory ID
    :return: None
    """
    execute(f"DELETE FROM inventory_table WHERE inventoryid={inventoryID};")


def updateItemByID(inventoryID: int, name: str, quantity: float, restockThreshold: float):
    """
    Sets the quantity and restock threshold for a specific inventory item based on its ID.
    :param inventoryID: inventory ID
    :param name: new name
    :param quantity: new quantity
    :param restockThreshold: new restock threshold
    :return: None
    """
    execute(f"UPDATE inventory_table SET name='{name}', quantity={quantity}, restockthreshold={restockThreshold} WHERE inventoryid={inventoryID};")


def addItemInventory(name: str, quantity: float, restockThreshold: float):
    """
    Inserts a new item into the inventory table along with its quantity and restock threshold.
    :param name: new name
    :param quantity: new quantity
    :param restockThreshold: new restock threshold
    :return: None
    """
    execute(f"INSERT INTO inventory_table (name, quantity, restockthreshold) VALUES ('{name}', {quantity}, {restockThreshold});")


# ===================== Reports =====================
def getProductUsage(startDate, endDate):
    """
    Retrieves the usage data for all inventory items over a specific time period.
    :param startDate: start date
    :param endDate: end date
    :return: List containing items and their usage
    """
    return execute(f"""SELECT inventory_table.name AS name,
            SUM(menu_part_table.quantity) AS quantity
        FROM (SELECT order_part_table.menuItemID
                FROM order_part_table
                INNER JOIN order_table
                ON order_table.orderID=order_part_table.orderID
                WHERE order_table.dateOrdered >= '{startDate}'
                    AND order_table.dateOrdered <= '{endDate}')
            AS menu_id
            INNER JOIN menu_part_table
            ON menu_id.menuItemID=menu_part_table.menuItemID
            INNER JOIN inventory_table
            ON menu_part_table.inventoryID=inventory_table.inventoryID
        GROUP BY name;""")


def getPairFrequency(startDate, endDate):
    """
    Returns the pairs of menu items that are purchased together most often.
    :param startDate: start date
    :param endDate: end date
    :return: List containing pairs of items frequently bought together
    """
    return execute(f"""Select menuItems1.name, menuItems2.name, COUNT (*) 
        AS frequency FROM order_part_table 
        AS t1 JOIN order_part_table AS t2 
        ON t1.orderid = t2.orderid 
        AND t1.menuitemid < t2.menuitemid 
        JOIN menu_items_table AS menuItems1 
        ON t1.menuitemid = menuItems1.menuitemid 
        JOIN menu_items_table AS menuItems2 
        ON t2.menuitemid = menuItems2.menuitemid 
        JOIN order_table AS orders 
        ON t1.orderid = orders.orderid 
        WHERE orders.dateordered >= '{startDate}' 
        AND orders.dateordered <= '{endDate}' 
        GROUP BY menuItems1.name, menuItems2.name 
        ORDER BY frequency DESC;""")


def getSalesHistory(startDate, endDate):
    """
    Retrieves store sales history over a specific time period.
    :param startDate: start date
    :param endDate: end date
    :return: List containing menu items and the amount of times bought
    """
    return execute(f"""SELECT mi.name, COUNT(op.menuitemid) AS sales
        FROM menu_items_table mi
        LEFT JOIN order_part_table op ON mi.menuitemid = op.menuitemid
        LEFT JOIN order_table o ON op.orderid = o.orderid
        WHERE o.dateordered >= '{startDate}' AND o.dateordered <= '{endDate}'
        GROUP BY mi.name
        ORDER BY sales DESC;""")


def getExcessItems(startDate):
    """
    Returns inventory items that did not sell as much as expected over a specific time period.
    :param startDate: start date
    :return: List containing inventory ID and quantity
    """
    return execute(f"""WITH ItemSales as (
            SELECT mpt.inventoryid, SUM(mpt.quantity) AS total_quantity_sold 
            FROM (
                SELECT 	opt.menuitemid 
                FROM order_table AS ot 
                INNER JOIN order_part_table AS opt ON ot.orderid = opt.orderid 
                WHERE ot.dateordered >= '{startDate}') 
            AS oid INNER JOIN menu_part_table as mpt ON oid.menuitemid = mpt.menuitemid 
            GROUP BY inventoryid
        ), Inventory as (
            SELECT * 
            FROM inventory_table 
            WHERE (inventoryid >= 14 AND inventoryid <= 47) OR inventoryid >= 50
        )
        SELECT
            i.name,
            COALESCE(s.total_quantity_sold, 0) AS quantitySold,
            i.quantity
        FROM
            Inventory i
        LEFT JOIN ItemSales s ON i.inventoryid = s.inventoryid
        WHERE COALESCE(s.total_quantity_sold, 0) <= (0.1 * i.quantity);""")


# ===================== Menu =====================
def getMenuItems():
    """
    Retrieves all menu items from the database.
    :return: List containing name, price, in stock, menu item ID, category, calories, and image ID
    """
    return execute("SELECT name, price, inStock, menuItemID, category, calories, imageID FROM menu_items_table;")


def getIngredients(menuItemID: int):
    """
    Retrieves all ingredients for a menu item from the database.
    :param menuItemID: menu item ID
    :return: List containing name, quantity, inventory ID, ingredient ID
    """
    return execute(f"SELECT  inventory_table.name AS name,\
                        menu_part_table.quantity AS quantity, \
                        inventory_table.inventoryID AS inventoryID, \
                        menu_part_table.uniqueID AS uniqueID \
                        FROM menu_part_table \
                        INNER JOIN inventory_table \
                        ON inventory_table.inventoryID=menu_part_table.inventoryID \
                        WHERE menu_part_table.menuItemID={menuItemID};")


def addMenuItem(name: str, price: float, inStock: bool, category: str, calories: int, imageID: int):
    """
    Inserts a new menu item into the menu items table.
    :param name: new name
    :param price: new price
    :param inStock: new stock status
    :param category: new category
    :param calories: new calories
    :param imageID: new image ID
    :return: None
    """
    execute(
        f"INSERT INTO menu_items_table (name, price, instock, category, calories, imageid) VALUES ('{name}', {price}, {inStock}, '{category}', {calories}, {imageID});")


def deleteMenuItem(itemID: int):
    """
    Deletes an item from the menu items table.
    :param itemID: item ID
    :return: None
    """
    execute(f"DELETE FROM menu_items_table WHERE menuItemID={itemID};")


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int, imageID: int):
    """
    Updates the attributes of an existing menu item.
    :param price: new price
    :param inStock: new stock status
    :param name: new name
    :param category: new category
    :param calories: new calorie count
    :param itemID: item ID
    :param imageID: new image ID
    :return: None
    """
    execute(
        f"UPDATE menu_items_table SET price={price}, inStock={inStock}, name='{name}', category='{category}', calories='{calories}', imageid={imageID} WHERE menuItemID={itemID};")


def addIngredient(menuItemID: int, inventoryID: int, quantity: float):
    """
    Adds a new ingredient to the menu part table.
    :param menuItemID: menu item ID associated with this ingredient
    :param inventoryID: inventory ID associated with this ingredient
    :param quantity: new quantity
    :return: None
    """
    execute(
        f"INSERT INTO menu_part_table (menuitemid, inventoryid, quantity) VALUES ({menuItemID}, {inventoryID}, {quantity});")


def deleteIngredient(uniqueID: int):
    """
    Deletes an ingredient from the menu part table.
    :param uniqueID: ingredient ID
    :return: None
    """
    execute(f"DELETE FROM menu_part_table WHERE uniqueID={uniqueID};")


def updateIngredient(quantity: float, ingredientID: int):
    """
    Sets the quantity of an ingredient based on its ID.
    :param quantity: new quantity
    :param ingredientID: ingredient ID
    :return: None
    """
    execute(f"UPDATE menu_part_table SET quantity={quantity} WHERE uniqueID={ingredientID}")


def getIngredientInventoryID(name: str):
    """
    Returns an ingredients ID based on its name.
    :param name: name
    :return: List containing inventory ID
    """
    return execute(f"SELECT inventoryID FROM inventory_table WHERE name='{name}';")


def getMenuItemCategories():
    """
    Gets categories of menu items, sorted by priority
    :return: List containing categories, ordered by priority (highest to lowest)
    """
    return execute(
        f"SELECT m.category FROM menu_items_table AS m LEFT JOIN category_priority AS p ON p.name=m.category GROUP BY m.category, p.priority ORDER BY p.priority;")


def addCategories(categories: str):
    """
    Inserts list of categories with priority into db only if category doesn't exist.
    :param categories: Must be of form ('category1', -1), ...., (categoryN, -1).
    :return:
    """
    execute(f"""INSERT INTO category_priority (name, priority)
                        VALUES
                            {categories}
                        ON CONFLICT (name) DO NOTHING;""")


def updateCategories(categories: str):
    """
    Updates category priority.
    :param categories: Must be of form ('category1', int(priority)), ..., ('categoryN', int(priority))
    :return:
    """
    execute(f"""UPDATE category_priority AS t SET
                            priority = c.priority
                        FROM (VALUES
                            {categories} 
                        ) as c(name, priority) 
                        WHERE c.name = t.name;""")


def removeUnusedCategories():
    """
    Removes categories from category_priority if they don't appear in menu_items_table.
    :return: None
    """
    execute(f"DELETE FROM category_priority row "
            f"WHERE NOT EXISTS ("
            f"    SELECT FROM menu_items_table mi"
            f"    WHERE mi.category = row.name"
            f");")


# ===================== User Management =====================
def getUsers():
    """
    Retrieves all user data from the database.
    NOTE: employee ID column from this is deprecated
    :return: List containing user ID, username, email, and employee ID
    """
    return execute(f"SELECT user_id, username, email, employee_id FROM user_table;")


def getEmployees():
    """
    Returns all employee data from the database.
    :return: List containing various employee properties
    """
    return execute(f"SELECT employeeID, name, isManager, isAdmin, email, phone, alt_email, pref_name, address, emergency_contact, pay_rate FROM employee_table;")


def addEmployee(name: str, isManager: bool, email: str, phoneNumber: str, altEmail: str, prefName: str, address: str, eContact: str, payRate: float, isAdmin: bool):
    """
    Inserts a new employee into the employee table.
    :param name: new name
    :param isManager: new manager status
    :param email: new email
    :param phoneNumber: new phone number
    :param altEmail: new alternate email
    :param prefName: new preferred name
    :param address: new address
    :param eContact: new emergency contact
    :param payRate: new pay rate
    :param isAdmin: new admin status
    :return: None
    """
    execute(f"INSERT INTO employee_table (name, ismanager, email, phone, alt_email, pref_name, address, emergency_contact, pay_rate, isadmin) "
            f"VALUES ('{name}', {isManager}, '{email}', '{phoneNumber}', '{altEmail}', '{prefName}', '{address}', '{eContact}', '{payRate}', {isAdmin});")


def updateEmployee(employeeID: int, name: str, isManager: bool, email: str, phoneNumber: str, altEmail: str, prefName: str, address: str, eContact: str, payRate: float, isAdmin: bool):
    """
    Updates the attributes of an existing employee.
    :param employeeID: employee ID
    :param name: new name
    :param isManager: new manager status
    :param email: new email
    :param phoneNumber: new phone number
    :param altEmail: new alternate email
    :param prefName: new preferred name
    :param address: new address
    :param eContact: new emergency contact
    :param payRate: new pay rate
    :param isAdmin: new admin status
    :return: None
    """
    execute(
        f"UPDATE employee_table "
        f"SET name='{name}',"
        f"    ismanager={isManager},"
        f"    isadmin={isAdmin},"
        f"    email='{email}',"
        f"    phone='{phoneNumber}',"
        f"    alt_email='{altEmail}',"
        f"    pref_name='{prefName}',"
        f"    address='{address}',"
        f"    emergency_contact='{eContact}',"
        f"    pay_rate={payRate} "
        f"WHERE employeeid={employeeID};")


def deleteEmployee(employeeID: int):
    """
    Deletes an employee from the employee table.
    :param employeeID: employee ID
    :return: None
    """
    execute(f"DELETE FROM employee_table WHERE employeeid={employeeID};")


def updateUser(userID: int, username: str, email: str, employeeID: int):
    """
    Updates the attributes of an existing user.
    :param userID: user ID
    :param username: new username
    :param email: new email
    :param employeeID: new employee ID (deprecated)
    :return:
    """
    execute(
        f"UPDATE user_table SET username='{username}', email='{email}', employee_id={employeeID} WHERE user_id={userID};")


# ===================== Orders =====================
def getOrders(startDate: str, endDate: str):
    """
    Retrieves all orders taken during a specific timeframe from the database.
    :param startDate: date in the format YYYY-MM-DD
    :param endDate: date in the format YYYY-MM-DD. Non-inclusive
    :return: List containing order ID, employee ID, date to be fulfilled, price, email, status
    """
    return execute(
        f"SELECT orderID, employeeID, dateOrdered, price, email, status FROM order_table WHERE dateordered >= '{startDate}' AND dateordered <= '{endDate}';")


def getOrderItemsByOrderID(orderID: int):
    """
    Retrieves order items by order ID
    :param orderID: order ID
    :return: List containing various order item properties
    """
    return execute(f"SELECT m.name AS drink_name, t1.name AS topping1, t2.name AS topping2, t3.name AS topping3, "
                   f"part.price AS price, part.sweetness AS sweetness, part.ice AS ice_level "
                   f"FROM order_part_table AS part "
                   f"LEFT JOIN menu_items_table AS m ON part.menuitemID=m.menuitemID "
                   f"LEFT JOIN topping_table AS t1 ON part.toppingID1=t1.toppingID "
                   f"LEFT JOIN topping_table AS t2 ON part.toppingID2=t2.toppingID "
                   f"LEFT JOIN topping_table AS t3 ON part.toppingID3=t3.toppingID "
                   f"WHERE part.orderID={orderID};")


def deleteOrder(orderID: int):
    """
    Deletes order from order_table
    :param orderID: order ID
    :return: None
    """
    execute(f"DELETE FROM order_table WHERE orderid={orderID};")


def deleteOrderParts(orderID: int):
    """
    Deletes order items from order_parts_table
    :param orderID: order ID
    :return: None
    """
    execute(f"DELETE FROM order_part_table WHERE orderid={orderID};")
