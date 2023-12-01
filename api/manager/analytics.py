from flask import Blueprint, jsonify, request, abort
from datetime import datetime, timedelta

from .analytics_helper import getProductUsage, getSalesHistory, getPairFrequency

analyticsAPIBlueprint = Blueprint("analytics", __name__)

@analyticsAPIBlueprint.route("/usage", methods = ['GET', 'POST'])
def productUsage():
    if request.method == 'GET':
        currDate = datetime.today().strftime('%Y-%m-%d')
        lastWeekDate = datetime.today() - timedelta(days=7)
        return jsonify(getProductUsage(lastWeekDate, currDate))
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

@analyticsAPIBlueprint.route("/sales", methods = ['GET', 'POST'])
def salesHistory():
    if request.method == 'GET':
        currDate = datetime.today().strftime('%Y-%m-%d')
        lastWeekDate = datetime.today() - timedelta(days=7)
        return jsonify(getSalesHistory(lastWeekDate, currDate))
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

            return jsonify(getSalesHistory(startDate, endDate))

@analyticsAPIBlueprint.route("/pair", methods = ['GET', 'POST'])
def pairFrequency():
    if request.method == 'GET':
        currDate = datetime.today().strftime('%Y-%m-%d')
        lastWeekDate = datetime.today() - timedelta(days=7)
        return jsonify(getPairFrequency(lastWeekDate, currDate))
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

            return jsonify(getPairFrequency(startDate, endDate))