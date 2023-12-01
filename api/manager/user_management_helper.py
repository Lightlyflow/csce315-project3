from api.db import manager_querier


def getUsers():
    result = manager_querier.getUsers()
    return result if result is not None else []


def getEmployees():
    result = manager_querier.getEmployees()
    return result if result is not None else []


def updateUser():
    pass


def addUser():
    pass


def updateEmployeeByID(employeeID: int, name: str, isManager: bool, email: str):
    manager_querier.updateEmployee(employeeID, name, isManager, email)


def deleteEmployeeByID(employeeID: int):
    manager_querier.deleteEmployee(employeeID)


def addEmployee(name: str, isManager: bool, email: str):
    # https://www.commandprompt.com/education/postgresql-insert-if-not-exists/
    # Add employee ID to existing user in user_table
    # Add employee entry to employee_table
    manager_querier.addEmployee(name, isManager, email)


"""
1. Add emails to employees
2. Change manager status to check email in employees
3. (?) Remove employee_id col in user table
"""
