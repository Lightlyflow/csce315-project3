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


def updateEmployee():
    pass


def removeEmployee():
    pass


def addEmployee():
    # Add employee ID to existing user in user_table
    # Add employee entry to employee_table
    pass
