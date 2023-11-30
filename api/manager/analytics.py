from flask import Blueprint, jsonify, request, abort

from .analytics_helper import getPairFrequency, getProductUsage

analyticsAPIBlueprint = Blueprint("analytics", __name__)

@analyticsAPIBlueprint.route("/usage", methods = ['GET', 'POST'])
def productUsage():
    if request.method == 'GET':
        return jsonify(getProductUsage('2023-09-26', '2023-10-3'))
    elif request.method == 'POST':
        method = request.args.get("method", default="")
        data = request.get_json()

        if method == 'UPDATE':
            startDate = ''
            endDate = ''

            try:
                startDate = data['startDate']
                endDate = data['endDate']
            except (ValueError, KeyError) as e:
                abort(400)

            return jsonify(getProductUsage(startDate, endDate))

@analyticsAPIBlueprint.route("/pair")
def pairFrequency():
    return jsonify(getPairFrequency())