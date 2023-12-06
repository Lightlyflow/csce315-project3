from flask import Blueprint, request, abort, jsonify

from .orders_helper import getOrders, getOrderItems, markOrder, deleteOrder

ordersAPIBlueprint = Blueprint("orders", __name__)


@ordersAPIBlueprint.route("/data", methods=['POST'])
def orderData():
    orders = getOrders()
    return jsonify(orders)


@ordersAPIBlueprint.route("/parts", methods=['POST'])
def orderPart():
    data = request.get_json()

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    parts = getOrderItems(orderID)
    return jsonify(parts)


@ordersAPIBlueprint.route("/mark", methods=['POST'])
def orderMark():
    data = request.get_json()

    try:
        orderID = int(data['orderid'])
        status = data['status']
    except (ValueError, KeyError):
        abort(400)

    parts = markOrder(orderID, status)
    return "marked", 201


@ordersAPIBlueprint.route("/delete", methods=['POST'])
def orderDelete():
    data = request.get_json()

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    deleteOrder(orderID)

    return "deleted", 201
