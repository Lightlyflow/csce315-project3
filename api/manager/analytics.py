from flask import Blueprint, jsonify, request, abort

from .analytics_helper import getPairFrequency, getProductUsage

analyticsAPIBlueprint = Blueprint("analytics", __name__)

@analyticsAPIBlueprint.route("/usage")
def productUsage():
    return jsonify(getProductUsage())

@analyticsAPIBlueprint.route("/pair")
def pairFrequency():
    return jsonify(getPairFrequency())