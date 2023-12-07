from flask import Blueprint, jsonify, request, abort
from flask_login import current_user

from .user_management_helper import getUsers, getEmployees, updateEmployeeByID, addEmployee, deleteEmployeeByID

userManagementBlueprint = Blueprint("userManagement", __name__)


@userManagementBlueprint.route("/users", methods=['GET'])
def users():
    """Sets up an endpoint to get the users.
    Returns a Response of the getUsers query."""
    return jsonify(getUsers())


@userManagementBlueprint.route("/employees", methods=['GET'])
def employees():
    """Sets up an endpoint to get the employees.
    Returns a Response of the getEmployees query."""
    return jsonify(getEmployees())


@userManagementBlueprint.route("/employees/update", methods=['POST'])
def employeeUpdate():
    """Sets up an endpoint to update an employee's information."""
    checkAdmin()

    data = request.get_json()

    try:
        employeeID = int(data['employeeid'])
        name = data['name']
        isManager = int(data['ismanager'])
        email = data['email']
        phoneNumber = data['phonenumber']
        altEmail = data['altemail']
        prefName = data['prefname']
        address = data['address']
        eContact = data['econtact']
        payRate = float(data['payrate'])
        isAdmin = int(data['isadmin'])
    except (ValueError, KeyError):
        abort(400)

    updateEmployeeByID(employeeID, name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate, isAdmin)
    return 'Updated employee', 201


@userManagementBlueprint.route("/employees/add", methods=['POST'])
def employeeAdd():
    """Sets up an endpoint to add an employee to the database."""
    checkAdmin()

    data = request.get_json()

    try:
        name = data['name']
        isManager = int(data['ismanager'])
        email = data['email']
        phoneNumber = data['phonenumber']
        altEmail = data['altemail']
        prefName = data['prefname']
        address = data['address']
        eContact = data['econtact']
        payRate = float(data['payrate'])
        isAdmin = int(data['isadmin'])
    except (ValueError, KeyError):
        abort(400)

    addEmployee(name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate, isAdmin)
    return 'Added employee', 201


@userManagementBlueprint.route("/employees/delete", methods=['POST'])
def employeeDelete():
    """Sets up an endpoint to delete an employee from the database."""
    checkAdmin()

    data = request.get_json()
    employeeID: int = -1

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    deleteEmployeeByID(employeeID)
    return 'Deleted employee', 201


def checkAdmin():
    """
    Checks whether a user is an admin or not
    :return: 403 if the user in not an admin
    """
    if current_user.is_authenticated and current_user.isAdmin:
        return
    abort(403)
