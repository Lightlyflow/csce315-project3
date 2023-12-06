if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv
    load_dotenv()

else:
    from .querier import execute

def getMenuItems():
    """Retrieves all menu items from the database."""
    return execute(f"SELECT name, category, price FROM menu_items_table WHERE instock = 't' ORDER BY category;")

def getCategoryNames():
    """Retrieves all menu category names from the database."""
    return execute(f"SELECT name FROM category_priority ORDER BY priority")

def getToppingNames():
    """Retrieves all topping names from the database."""
    return execute(f"Select name from topping_table;")

def getMenuItemId(name):
    """Returns a menu item ID based on its name."""
    return execute(f"SELECT menuitemid FROM menu_items_table WHERE name='{name}';")

def getMenuCategories():
    """Retrieves all menu categories from the database."""
    return execute(f"SELECT name FROM category_priority order by priority;")

if __name__ == '__main__':
    # If you want to run this, delete the period in front of the import statements in this file
    # but make sure to add them back
    res = getUserByEmail("test@gmail.com")
    print(res)