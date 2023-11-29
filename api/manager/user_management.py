from flask import Blueprint, jsonify, request, abort

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
    data = request.get_json()
    employeeID = -1
    name = ""
    isManager = False
    email = ""

    try:
        employeeID = int(data['employeeid'])
        name = data['name']
        isManager = int(data['ismanager'])
        email = data['email']
    except (ValueError, KeyError):
        abort(400)

    updateEmployeeByID(employeeID, name, isManager, email)
    return 'Updated employee', 201


@userManagementBlueprint.route("/employees/add", methods=['POST'])
def employeeAdd():
    data = request.get_json()
    name = ""
    isManager = False
    email = ""

    try:
        name = data['name']
        isManager = int(data['ismanager'])
        email = data['email']
    except (ValueError, KeyError):
        abort(400)

    addEmployee(name, isManager, email)
    return 'Added employee', 201


@userManagementBlueprint.route("/employees/delete", methods=['POST'])
def employeeDelete():
    data = request.get_json()
    employeeID: int = -1

    try:
        employeeID = int(data['employeeid'])
    except (ValueError, KeyError):
        abort(400)

    deleteEmployeeByID(employeeID)
    return 'Deleted employee', 201
