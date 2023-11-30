from flask import Blueprint, request, abort, jsonify

from .orders_helper import getOrders

ordersAPIBlueprint = Blueprint("orders", __name__)


@ordersAPIBlueprint.route("/data", methods=['POST'])
def orderData():
    data = request.get_json()
    startDate: str | None = None
    endDate: str | None = None

    try:
        startDate = data['startdate']
        endDate = data['enddate']
    except (ValueError, KeyError) as e:
        abort(400)

    orders = getOrders(startDate, endDate)

    return jsonify(orders)
