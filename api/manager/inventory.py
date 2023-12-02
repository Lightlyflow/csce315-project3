from flask import Blueprint, jsonify, request, abort

from .inventory_helper import orderItems, orderAllItems, getInventory, getLowStock, updateThresholds, \
    deleteInventoryItem, updateInventoryItem, addInventoryItem

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


@inventoryAPIBlueprint.route("/delete", methods=['POST'])
def inventoryDelete():
    data = request.get_json()
    inventoryID = -1

    try:
        inventoryID = int(data['inventoryid'])
    except (ValueError, KeyError):
        abort(400)

    deleteInventoryItem(inventoryID)
    return "Deleted", 201


@inventoryAPIBlueprint.route("/update", methods=['POST'])
def inventoryUpdate():
    data = request.get_json()
    inventoryID = -1
    name = ""
    quantity = 0
    restockThreshold = 0

    try:
        inventoryID = int(data['inventoryid'])
        name = data['name']
        quantity = float(data['quantity'])
        restockThreshold = float(data['restockthreshold'])
    except (ValueError, KeyError):
        abort(400)

    updateInventoryItem(inventoryID, name, quantity, restockThreshold)
    return "Updated", 201


@inventoryAPIBlueprint.route("/add", methods=['POST'])
def inventoryAdd():
    data = request.get_json()
    name = ""
    quantity = 0
    restockThreshold = 0

    try:
        name = data['name']
        quantity = float(data['quantity'])
        restockThreshold = float(data['restockthreshold'])
    except (ValueError, KeyError):
        abort(400)

    addInventoryItem(name, quantity, restockThreshold)
    return "Added", 201
