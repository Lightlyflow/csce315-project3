from flask import Blueprint, request, abort, jsonify

from .orders_helper import getOrders, getOrderItems

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


@ordersAPIBlueprint.route("/parts", methods=['POST'])
def orderPart():
    data = request.get_json()
    orderID = -1

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    parts = getOrderItems(orderID)
    return jsonify(parts)
