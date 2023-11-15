from flask import Blueprint, request, jsonify, abort
from .menu_helper import getMenuItems, getIngredients, addMenuItem, delMenuItem, updateMenuItem

menuAPIBlueprint = Blueprint("menu", __name__)


@menuAPIBlueprint.route("/menuitems", methods=['GET', 'POST'])
def menuItems():
    if request.method == 'GET':
        return jsonify(getMenuItems())
    elif request.method == 'POST':
        method = request.args.get("method", default="")
        data = request.get_json()

        if method == 'ADD':
            name = ''
            price = 0
            inStock = 'false'
            category = ''
            calories = 0

            try:
                name = data['name']
                price = float(data['price'])
                inStock = data['instock']
                category = data['category']
                calories = int(data['calories'])
            except (ValueError, KeyError) as e:
                abort(400)

            addMenuItem(name, price, inStock, category, calories)
            return "Added Menu Item", 201
        elif method == 'DEL':
            itemID = -1

            try:
                itemID = int(data['itemid'])
            except (ValueError, KeyError) as e:
                abort(400)

            delMenuItem(itemID)
            return "Deleted Menu Item", 201
        elif method == 'UPDATE':
            name = ''
            price = 0
            inStock = 'false'
            category = ''
            calories = 0
            itemID = -1

            try:
                name = data['name']
                price = float(data['price'])
                inStock = data['instock']
                category = data['category']
                calories = int(data['calories'])
                itemID = int(data['itemid'])
            except (ValueError, KeyError) as e:
                abort(400)

            updateMenuItem(price, inStock, name, category, calories, itemID)
            return "Updated Menu Item", 201
        abort(400)


@menuAPIBlueprint.route("/ingredients", methods=['GET', 'POST'])
def ingredients():
    if request.method == 'GET':
        menuItemID = 0
        try:
            menuItemID = int(request.args['menuitemid'])
        except (ValueError, KeyError) as e:
            abort(400)
        return jsonify(getIngredients(menuItemID))
    elif request.method == 'POST':
        method = request.args.get("method", default="")
        data = request.get_json()

        if method == 'ADD':
            # TODO :: Check if already exists in db!
            pass
        elif method == 'DEL':
            pass
        elif method == 'UPDATE':
            pass
        abort(400)
