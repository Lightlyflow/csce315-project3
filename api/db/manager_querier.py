from .querier import execute


# ===================== Inventory =====================
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
    execute(f"INSERT INTO menu_items_table (name, price, instock, category, calories) VALUES ('{name}', {price}, {inStock}, '{category}', {calories});")


def deleteMenuItem(itemID: int):
    execute(f"DELETE FROM menu_items_table WHERE menuItemID={itemID};")


def updateMenuItem(price: int, inStock: bool, name: str, category: str, calories: int, itemID: int):
    execute(f"UPDATE menu_items_table SET price={price}, inStock={inStock}, name='{name}', category='{category}', calories='{calories}' WHERE menuItemID={itemID};")


def addIngredient(menuItemID: int, inventoryID: int, quantity: float):
    execute(f"INSERT INTO menu_part_table (menuitemid, inventoryid, quantity) VALUES ({menuItemID}, {inventoryID}, {quantity});")


def deleteIngredient(uniqueID: int):
    execute(f"DELETE FROM menu_part_table WHERE uniqueID={uniqueID};")


def updateIngredient(quantity: float, ingredientID: int):
    execute(f"UPDATE menu_part_table SET quantity={quantity} WHERE uniqueID={ingredientID}")

