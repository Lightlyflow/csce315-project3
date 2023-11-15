from flask import Blueprint, jsonify, request, abort

from .analytics_helper import getPairReport

analyticsAPIBlueprint = Blueprint("analytics", __name__)

@analyticsAPIBlueprint.route("/pair")
def pairReport():
    return jsonify(getPairReport())