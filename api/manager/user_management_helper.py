from api.db import manager_querier


def getUsers():
    """
    Calls the querier and returns the users from the database.
    :return: List of users
    """
    result = manager_querier.getUsers()
    return result if result is not None else []


def getEmployees():
    """
    Calls the querier and returns the employees from the database.
    :return: List of employees
    """
    result = manager_querier.getEmployees()
    return result if result is not None else []


def updateEmployeeByID(employeeID: int, name: str, isManager: bool, email: str, phoneNumber: str, altEmail: str, prefName: str, address: str, eContact: str, payRate: float, isAdmin: bool):
    """
    Calls the querier and updates an employee's information in the database.
    :param employeeID: employee ID
    :param name: new name
    :param isManager: new manager status
    :param email: new email
    :param phoneNumber: new phone number
    :param altEmail: new alternate email
    :param prefName: new preferred name
    :param address: new address
    :param eContact: new emergency contact
    :param payRate: new pay rate
    :param isAdmin: new admin status
    :return: None
    """
    manager_querier.updateEmployee(employeeID, name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate, isAdmin)


def deleteEmployeeByID(employeeID: int):
    """
    Calls the querier and deleted an employee by id from the database.
    :param employeeID: employee ID
    :return: None
    """
    manager_querier.deleteEmployee(employeeID)


def addEmployee(name: str, isManager: bool, email: str, phoneNumber: str, altEmail: str, prefName: str, address: str, eContact: str, payRate: float, isAdmin: bool):
    """
    Calls the querier and adds an employee to the database.
    :param name: new name
    :param isManager: new manager status
    :param email: new email
    :param phoneNumber: new phone number
    :param altEmail: new alternate email
    :param prefName: new preferred name
    :param address: new address
    :param eContact: new emergency contact
    :param payRate: new pay rate
    :param isAdmin: new admin status
    :return: None
    """
    manager_querier.addEmployee(name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate, isAdmin)


"""
1. Add emails to employees
2. Change manager status to check email in employees
3. (?) Remove employee_id col in user table
"""
