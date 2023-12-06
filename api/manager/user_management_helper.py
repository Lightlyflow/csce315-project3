from api.db import manager_querier


def getUsers():
    """Calls the querier and returns the users from the database."""
    result = manager_querier.getUsers()
    return result if result is not None else []


def getEmployees():
    """Calls the querier and returns the employees from the database."""
    result = manager_querier.getEmployees()
    return result if result is not None else []


def updateUser():
    pass


def addUser():
    pass


def updateEmployeeByID(employeeID: int, name: str, isManager: bool, email: str, phoneNumber: str, altEmail: str, prefName: str, address: str, eContact: str, payRate: float, isAdmin: bool):
    """Calls the querier and updates an employee's information in the database."""
    manager_querier.updateEmployee(employeeID, name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate, isAdmin)


def deleteEmployeeByID(employeeID: int):
    """Calls the querier and deleted an employee by id from the database."""
    manager_querier.deleteEmployee(employeeID)


def addEmployee(name: str, isManager: bool, email: str, phoneNumber: str, altEmail: str, prefName: str, address: str, eContact: str, payRate: float, isAdmin: bool):
    """Calls the querier and adds an employee to the database."""
    manager_querier.addEmployee(name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate, isAdmin)


"""
1. Add emails to employees
2. Change manager status to check email in employees
3. (?) Remove employee_id col in user table
"""
