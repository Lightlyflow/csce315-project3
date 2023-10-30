from .querier import execute


def getUserByEmail(email: str):
    return execute(f"SELECT user_id, username, email, employee_id FROM user_table WHERE email='{email}';")


def getUserById(userId: int):
    return execute(f"SELECT user_id, username, email, employee_id FROM user_table WHERE user_id={userId};")


def addUser(email: str):
    username = email.split("@")[0]
    execute(f"INSERT INTO user_table(username, email) VALUES ('{username}', '{email}');",
            getRet=False)


def getEmployeeById(employeeId: int):
    return execute(f"SELECT name, employeeId, isManager FROM employee_table WHERE employeeid={employeeId};")


def _createUserTable():
    """Creates user_table with auto incrementing user_id, and other properties."""
    execute(f"CREATE TABLE IF NOT EXISTS user_table ("
            f"  user_id SERIAL PRIMARY KEY,"
            f"  username text,"
            f"  email text,"
            f"  employee_id int"
            f");",
            getRet=False)


if __name__ == '__main__':
    # If you want to run this, delete the period in front of the import statements in this file
    # but make sure to add them back
    res = getUserByEmail("test@gmail.com")
    print(res)
