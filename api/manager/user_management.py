from flask import Blueprint, jsonify

from .user_management_helper import getUsers, getEmployees

userManagementBlueprint = Blueprint("userManagement", __name__)


@userManagementBlueprint.route("/users", methods=['GET'])
def users():
    return jsonify(getUsers())


@userManagementBlueprint.route("/employees", methods=['GET'])
def employees():
    return jsonify(getEmployees())

