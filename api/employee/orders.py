from flask import Blueprint, request, abort, jsonify

from .orders_helper import getOrders, getOrderItems, markOrder, deleteOrder

ordersAPIBlueprint = Blueprint("orders", __name__)


@ordersAPIBlueprint.route("/data", methods=['POST'])
def orderData():
    """
    Endpoint for getting list of today's orders
    :return: Response of unfulfilled orders
    """
    orders = getOrders()
    return jsonify(orders)


@ordersAPIBlueprint.route("/parts", methods=['POST'])
def orderPart():
    """
    Endpoint for getting order items from an order
    :return: Response of order items in an order or 400 if invalid arguments
    """
    data = request.get_json()

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    parts = getOrderItems(orderID)
    return jsonify(parts)


@ordersAPIBlueprint.route("/mark", methods=['POST'])
def orderMark():
    """
    Endpoint for marking an order
    :return: 400 if invalid arguments or 201 if success
    """
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
    """
    Endpoint for deleting an order
    :return: 400 if invalid arguments or 201 on success
    """
    data = request.get_json()

    try:
        orderID = int(data['orderid'])
    except (ValueError, KeyError):
        abort(400)

    deleteOrder(orderID)

    return "deleted", 201
