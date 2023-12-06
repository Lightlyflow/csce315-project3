from .querier import execute

def getUserByEmail(email: str):
    """Returns user from database given their associated email."""
    return execute(f"SELECT user_id, username FROM user_table WHERE email='{email}';")

def getUserById(userId: int):
    """Returns user from database given their associated ID."""
    return execute(f"SELECT user_id, username, email, employee_id FROM user_table WHERE user_id={userId};")

def addUser(email: str):
    """Adds user to database based on given email."""
    username = email.split("@")[0]
    execute(f"INSERT INTO user_table(username, email) VALUES ('{username}', '{email}');",
            getRet=False)

def getEmployeeByEmail(email: str):
    """Returns employee from database given their associated email."""
    return execute(f"SELECT name, employeeID, isManager, pref_name FROM employee_table WHERE email='{email}';")

def _createUserTable():
    """Creates user_table with auto incrementing user_id, and other properties."""
    execute(f"CREATE TABLE IF NOT EXISTS user_table ("
            f"  user_id SERIAL PRIMARY KEY,"
            f"  username text,"
            f"  email text,"
            f"  employee_id int"
            f");",
            getRet=False)


def emailExists(email: str):
    """Checks if email exists in either users or employees. Returns [[0]] if not found"""
    return execute(f"SELECT count(*) FROM user_table WHERE EXISTS ( SELECT 1 FROM employee_table WHERE email='{email}' ) OR EXISTS ( SELECT 1 FROM user_table WHERE email='{email}' );")
