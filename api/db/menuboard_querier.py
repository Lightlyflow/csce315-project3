if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv

    load_dotenv()

else:
    from .querier import execute


def getMenuItems():
    """
    Retrieves all menu items that are in stock from the database.
    :return: List containing name, category, and price
    """
    return execute(f"SELECT name, category, price FROM menu_items_table WHERE instock = 't' ORDER BY category;")


def getCategoryNames():
    """
    Retrieves all menu category names from the database.
    :return: List of categories, ordered by priority
    """
    return execute(f"SELECT name FROM category_priority ORDER BY priority")


def getToppingNames():
    """
    Retrieves all topping names from the database.
    :return: List of topping names
    """
    return execute(f"Select name from topping_table;")


def getMenuItemId(name):
    """
    Returns a menu item ID based on its name.
    :param name: menu item name
    :return: List containing menu item ID
    """
    return execute(f"SELECT menuitemid FROM menu_items_table WHERE name='{name}';")


def getMenuCategories():
    """
    Retrieves all menu categories from the database.
    :return: List of categories, ordered by priority
    """
    return execute(f"SELECT name FROM category_priority order by priority;")
