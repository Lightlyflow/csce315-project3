from flask import Blueprint, render_template, jsonify, request, abort
from .manager_helper import getInventory, getLowStock, orderItems

managerBlueprint = Blueprint("manager", __name__, template_folder="templates", static_folder="static")


@managerBlueprint.route("/", methods=["GET"])
def home():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/analytics", methods=["GET"])
def analytics():
    return render_template("manager_analytics.html")


@managerBlueprint.route("/employees", methods=["GET"])
def employees():
    return render_template("manager_employees.html")


@managerBlueprint.route("/inventory", methods=["GET"])
def inventory():
    allInventory = getInventory()
    lowStock = getLowStock()
    return render_template("manager_inventory.html",
                           inventory=allInventory,
                           lowStock=lowStock)


@managerBlueprint.route("/menu", methods=["GET"])
def menu():
    return render_template("manager_menu.html")


# POST Endpoints

@managerBlueprint.route("/inventory/order")
def inventoryOrder():
    data = request.get_json()
    amount: float = 0
    items: [str] = []

    try:
        amount = float(data['amount'])
        items = data['items']
    except (ValueError, KeyError) as e:
        abort(400)

    # orderItems(amount, items)

    return "Updated", 201


@managerBlueprint.route("/inventory/stock")
def inventoryStock():
    lowStock: bool = request.args.get("low", type=bool, default=False)

    if lowStock:
        return jsonify(getLowStock())
    return jsonify(getInventory())
