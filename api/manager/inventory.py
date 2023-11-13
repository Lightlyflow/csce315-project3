from flask import Blueprint, jsonify, request, abort

from .inventory_helper import orderItems, orderAllItems, getInventory, getLowStock, updateThresholds

inventoryAPIBlueprint = Blueprint("inventory", __name__)


@inventoryAPIBlueprint.route("/order", methods=['POST'])
def inventoryOrder():
    data = request.get_json()
    amount: float = 0
    items: [str] = []

    try:
        amount = float(data['amount'])
        items = data['items']
    except (ValueError, KeyError) as e:
        abort(400)

    orderItems(amount, items)

    return "Updated", 201


@inventoryAPIBlueprint.route("/orderall", methods=['POST'])
def inventoryOrderAll():
    data = request.get_json()
    amount: float = 0

    try:
        amount = float(data['amount'])
    except (ValueError, KeyError) as e:
        abort(400)

    orderAllItems(amount)

    return "Updated", 201


@inventoryAPIBlueprint.route("/stock")
def inventoryStock():
    lowStock: bool = request.args.get("low", type=bool, default=False)

    if lowStock:
        return jsonify(getLowStock())
    return jsonify(getInventory())


@inventoryAPIBlueprint.route("/threshold", methods=['POST'])
def inventoryThreshold():
    data = request.get_json()
    names: str = ""
    threshold: float = 0

    try:
        threshold = float(data['threshold'])
        names = data['names']
    except (ValueError, KeyError) as e:
        abort(400)

    updateThresholds(names, threshold)

    return "Updated", 201

