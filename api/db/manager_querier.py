from .querier import execute


# ===================== Inventory =====================
def getInventory():
    return execute("SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table;")


def getLowStock():
    return execute(
        "SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table WHERE quantity<restockThreshold;")


def createIngredient(name: str):
    execute(f"INSERT INTO inventory_table (name, quantity) VALUES ('{name}', 0);")


def orderItem(amount: float, name: str):
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount} WHERE name='{name}';")


def orderAllItems(amount: float):
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount};")


def updateThreshold(name: str, amount: float):
    execute(f"UPDATE inventory_table SET restockThreshold={amount} WHERE name='{name}';")


# ===================== Reports =====================
def getProductUsage(startDate, endDate):
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
    return execute(f"""SELECT mi.name, COUNT(op.menuitemid) AS sales
        FROM menu_items_table mi
        LEFT JOIN order_part_table op ON mi.menuitemid = op.menuitemid
        LEFT JOIN order_table o ON op.orderid = o.orderid
        WHERE o.dateordered >= '{startDate}' AND o.dateordered <= '{endDate}'
        GROUP BY mi.name
        ORDER BY sales DESC;""")

def getExcessItems(startDate):
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
    return execute("SELECT name, price, inStock, menuItemID, category, calories FROM menu_items_table;")


def getIngredients(menuItemID: int):
    return execute(f"SELECT  inventory_table.name AS name,\
                        menu_part_table.quantity AS quantity, \
                        inventory_table.inventoryID AS inventoryID, \
                        menu_part_table.uniqueID AS uniqueID \
                        FROM menu_part_table \
                        INNER JOIN inventory_table \
                        ON inventory_table.inventoryID=menu_part_table.inventoryID \
                        WHERE menu_part_table.menuItemID={menuItemID};")


def addMenuItem(name: str, price: float, inStock: bool, category: str, calories: int):
    execute(
        f"INSERT INTO menu_items_table (name, price, instock, category, calories) VALUES ('{name}', {price}, {inStock}, '{category}', {calories});")


def deleteMenuItem(itemID: int):
    execute(f"DELETE FROM menu_items_table WHERE menuItemID={itemID};")


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int):
    execute(
        f"UPDATE menu_items_table SET price={price}, inStock={inStock}, name='{name}', category='{category}', calories='{calories}' WHERE menuItemID={itemID};")


def addIngredient(menuItemID: int, inventoryID: int, quantity: float):
    """DOES NOT CHECK IF INGREDIENT ALREADY EXISTS!!!"""
    execute(
        f"INSERT INTO menu_part_table (menuitemid, inventoryid, quantity) VALUES ({menuItemID}, {inventoryID}, {quantity});")


def deleteIngredient(uniqueID: int):
    execute(f"DELETE FROM menu_part_table WHERE uniqueID={uniqueID};")


def updateIngredient(quantity: float, ingredientID: int):
    execute(f"UPDATE menu_part_table SET quantity={quantity} WHERE uniqueID={ingredientID}")


def getIngredientInventoryID(name: str):
    return execute(f"SELECT inventoryID FROM inventory_table WHERE name='{name}';")


# ===================== User Management =====================
def getUsers():
    return execute(f"SELECT user_id, username, email, employee_id FROM user_table;")


def getEmployees():
    return execute(f"SELECT employeeID, name, isManager, email FROM employee_table;")


def addEmployee(name: str, isManager: bool, email: str):
    execute(f"INSERT INTO employee_table (name, ismanager, email) VALUES ('{name}', {isManager}, '{email}');")


def updateEmployee(employeeID: int, name: str, isManager: bool, email: str):
    execute(f"UPDATE employee_table SET name='{name}', ismanager={isManager}, email='{email}' WHERE employeeid={employeeID};")


def deleteEmployee(employeeID: int):
    execute(f"DELETE FROM employee_table WHERE employeeid={employeeID};")


def updateUser(userID: int, username: str, email: str, employeeID: int):
    execute(f"UPDATE user_table SET username='{username}', email='{email}', employee_id={employeeID} WHERE user_id={userID};")
