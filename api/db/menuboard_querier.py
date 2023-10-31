if __name__ == '__main__':
    from querier import execute
    from dotenv import load_dotenv
    load_dotenv()

else:
    from .querier import execute

def getMenuItems():
    return execute(f"SELECT name, category FROM menu_items_table;")