from flask import Blueprint, jsonify, request, abort

from .inventory_helper import orderItems, orderAllItems, getInventory, getLowStock, updateThresholds, \
    deleteInventoryItem, updateInventoryItem, addInventoryItem

inventoryAPIBlueprint = Blueprint("inventory", __name__)


@inventoryAPIBlueprint.route("/order", methods=['POST'])
def inventoryOrder():
    """Sets up an endpoint for ordering items in the inventory. 
    Calls orderItems with provided amount and items."""
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
    """Sets up an endpoint for ordering all items in the inventory. 
    Calls orderAllItems with the provided amount."""
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
    """Sets up an endpoint for inventory stock. 
    Calls low stock if inventory is option is set, else gets the inventory."""
    lowStock: bool = request.args.get("low", type=bool, default=False)

    if lowStock:
        return jsonify(getLowStock())
    return jsonify(getInventory())


@inventoryAPIBlueprint.route("/threshold", methods=['POST'])
def inventoryThreshold():
    """Sets up an endpoint for the inventory threshold.
    Calls updateThresholds with the provided names and thresholds."""
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
    """Sets up an endpoint to delete items from the database.
    Calls deleteInventoryItem with the provided id."""
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
    """Sets up an endpoint to update items in the inventory.
    Calls updateInventoryItem with the provided id, name, quantity, and threshold."""
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
    """Sets up an endpoint to add inventory items to the database.
    Calls addInventoryItem with the provided name, quantity, and restock threshold."""
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
