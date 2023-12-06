from flask import Blueprint, jsonify, request, abort
from flask_login import current_user

from .user_management_helper import getUsers, getEmployees, updateEmployeeByID, addEmployee, deleteEmployeeByID

userManagementBlueprint = Blueprint("userManagement", __name__)


@userManagementBlueprint.route("/users", methods=['GET'])
def users():
    return jsonify(getUsers())


@userManagementBlueprint.route("/employees", methods=['GET'])
def employees():
    return jsonify(getEmployees())


@userManagementBlueprint.route("/employees/update", methods=['POST'])
def employeeUpdate():
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
    if current_user.is_authenticated and current_user.isAdmin:
        return
    abort(403)
