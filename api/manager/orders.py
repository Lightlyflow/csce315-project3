from flask import Blueprint, request, abort, jsonify

from .orders_helper import getOrders, getOrderItems, deleteOrder

ordersAPIBlueprint = Blueprint("orders", __name__)


@ordersAPIBlueprint.route("/data", methods=['POST'])
def orderData():
    """Sets up an endpoint to retrieve order data.
    Gets data in the range of startDate to endDate."""
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
    """Sets up an endpoint to retrieve order part data.
    Gets data by the order id."""
    data = request.get_json()
    orderID = -1

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    parts = getOrderItems(orderID)
    return jsonify(parts)


@ordersAPIBlueprint.route("/delete", methods=['POST'])
def orderDelete():
    """Sets up an endpoint to delete order data."""
    data = request.get_json()
    orderID = -1

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    deleteOrder(orderID)

    return "deleted", 201
