if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv
    load_dotenv()

else:
    from .querier import execute



def getMenuItems():
    return execute(f"SELECT name, category FROM menu_items_table;")

if __name__ == '__main__':
    # If you want to run this, delete the period in front of the import statements in this file
    # but make sure to add them back
    res = getUserByEmail("test@gmail.com")
    print(res)