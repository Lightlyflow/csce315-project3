from flask import Blueprint, jsonify, request, abort

from .user_management_helper import getUsers, getEmployees, updateEmployeeByID, addEmployee, deleteEmployeeByID

userManagementBlueprint = Blueprint("userManagement", __name__)


@userManagementBlueprint.route("/users", methods=['GET'])
def users():
    """Sets up an endpoint to get the users.
    Returns a jsonification of the getUsers query."""
    return jsonify(getUsers())


@userManagementBlueprint.route("/employees", methods=['GET'])
def employees():
    """Sets up an endpoint to get the employees.
    Returns a jsonification of the getEmployees query."""
    return jsonify(getEmployees())


@userManagementBlueprint.route("/employees/update", methods=['POST'])
def employeeUpdate():
    """Sets up an endpoint to update an employee's information."""
    data = request.get_json()
    employeeID = -1
    name = ""
    isManager = False
    email = ""
    phoneNumber = ""
    altEmail = ""
    prefName = ""
    address = ""
    eContact = ""
    payRate = 0

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
    except (ValueError, KeyError):
        abort(400)

    updateEmployeeByID(employeeID, name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate)
    return 'Updated employee', 201


@userManagementBlueprint.route("/employees/add", methods=['POST'])
def employeeAdd():
    """Sets up an endpoint to add an employee to the database."""
    data = request.get_json()
    name = ""
    isManager = False
    email = ""
    phoneNumber = ""
    altEmail = ""
    prefName = ""
    address = ""
    eContact = ""
    payRate = 0

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
    except (ValueError, KeyError):
        abort(400)

    addEmployee(name, isManager, email, phoneNumber, altEmail, prefName, address, eContact, payRate)
    return 'Added employee', 201


@userManagementBlueprint.route("/employees/delete", methods=['POST'])
def employeeDelete():
    """Sets up an endpoint to delete an employee from the database."""
    data = request.get_json()
    employeeID: int = -1

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    deleteEmployeeByID(employeeID)
    return 'Deleted employee', 201
