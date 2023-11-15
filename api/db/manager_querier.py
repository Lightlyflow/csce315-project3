from .querier import execute


def getInventory():
    return execute("SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table;")


def getLowStock():
    return execute(
        "SELECT inventoryID, name, quantity, restockThreshold FROM inventory_table WHERE quantity<restockThreshold;")


def orderItem(amount: float, name: str):
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount} WHERE name='{name}';")


def orderAllItems(amount: float):
    execute(f"UPDATE inventory_table SET quantity=quantity+{amount};")


def updateThreshold(name: str, amount: float):
    execute(f"UPDATE inventory_table SET restockThreshold={amount} WHERE name='{name}';")

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

