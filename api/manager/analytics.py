from flask import Blueprint, jsonify, request, abort
from datetime import datetime, timedelta

from .analytics_helper import getProductUsage, getSalesHistory, getPairFrequency, getExcessItems

analyticsAPIBlueprint = Blueprint("analytics", __name__)

@analyticsAPIBlueprint.route("/usage", methods = ['GET', 'POST'])
def productUsage():
    """Sets up an endpoint for the product usage report. 
    Returns the jsonification of the product usage query to
    be displayed. Can specify the dates or use the default 
    value of the last 7 days."""
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
    """Sets up an endpoint for the sales history report. 
    Returns the jsonification of the sales history query to
    be displayed. Can specify the dates or use the default 
    value of the last 7 days."""
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

@analyticsAPIBlueprint.route("/excess", methods = ['GET', 'POST'])
def excessItems():
    """Sets up an endpoint for the excess items report. 
    Returns the jsonification of the excess items query to
    be displayed. Can specify the date or use the default 
    value of 7 days ago."""
    if request.method == 'GET':
        lastWeekDate = datetime.today() - timedelta(days=7)
        return jsonify(getExcessItems(lastWeekDate))
    elif request.method == 'POST':
        method = request.args.get("method", default="")
        data = request.get_json()

        if method == 'UPDATE':
            startDate = ''

            try:
                startDate = data['startDate']
            except (ValueError, KeyError) as e:
                abort(400)

            return jsonify(getExcessItems(startDate))

@analyticsAPIBlueprint.route("/pair", methods = ['GET', 'POST'])
def pairFrequency():
    """Sets up an endpoint for the pair frequency report. 
    Returns the jsonification of the pair frequency query to
    be displayed. Can specify the dates or use the default 
    value of the last 7 days."""
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