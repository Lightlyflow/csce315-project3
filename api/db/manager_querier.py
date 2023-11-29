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
def getPairReport():
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
            WHERE orders.dateordered > '2023-09-01' 
            AND orders.dateordered < '2023-10-01' 
            GROUP BY menuItems1.name, menuItems2.name 
            ORDER BY frequency DESC;""")


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
