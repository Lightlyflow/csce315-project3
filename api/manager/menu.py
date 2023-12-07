from flask import Blueprint, request, jsonify, abort
from .menu_helper import getMenuItems, getIngredients, addMenuItem, delMenuItem, updateMenuItem, delIngredient, \
    addIngredient, updateIngredient, getMenuCategories, addMenuCategories, updateMenuCategoriesOrder

menuAPIBlueprint = Blueprint("menu", __name__)


@menuAPIBlueprint.route("/menuitems", methods=['GET', 'POST'])
def menuItems():
    """Sets up an endpoint for the menu items.
    Handles methods for adding, updating, and deleting
    menu items. Returns statuses, or a Response
    of the getMenuItems query."""
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
            imageID = -1

            try:
                name = data['name']
                price = float(data['price'])
                inStock = data['instock']
                category = data['category']
                calories = int(data['calories'])
                imageID = int(data['imageid'])
            except (ValueError, KeyError) as e:
                abort(400)

            addMenuItem(name, price, inStock, category, calories, imageID)
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
            imageID = -1

            try:
                name = data['name']
                price = float(data['price'])
                inStock = data['instock']
                category = data['category']
                calories = int(data['calories'])
                itemID = int(data['itemid'])
                imageID = int(data['imageid'])
            except (ValueError, KeyError) as e:
                abort(400)

            updateMenuItem(price, inStock, name, category, calories, itemID, imageID)
            return "Updated Menu Item", 201
        abort(400)


@menuAPIBlueprint.route("/ingredients", methods=['GET', 'POST'])
def ingredients():
    """Sets up an endpoint for the menu item ingredients.
    Handles methods for adding, updating, and deleting
    menu item ingredients. Returns statuses, or a Response
    of the getIngredients query."""
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
            menuItemID = -1
            name = ''
            quantity = 0

            try:
                menuItemID = data['menuitemid']
                name = data['name']
                quantity = data['quantity']
            except (ValueError, KeyError) as e:
                abort(400)

            addIngredient(menuItemID, name, quantity)
            return 'Added ingredient', 201
        elif method == 'DEL':
            uniqueID = -1

            try:
                uniqueID = int(data['uniqueid'])
            except (ValueError, KeyError) as e:
                abort(400)

            delIngredient(uniqueID)
            return 'Deleted ingredient', 201
        elif method == 'UPDATE':
            quantity = 0
            uniqueID = -1

            try:
                quantity = float(data['quantity'])
                uniqueID = int(data['uniqueid'])
            except (ValueError, KeyError) as e:
                abort(400)

            updateIngredient(quantity, uniqueID)
            return 'Updated ingredient', 201
        abort(400)


@menuAPIBlueprint.route("/categories", methods=['GET', 'POST'])
def categories():
    """Sets up an endpoint for the menu item categories.
    Handles methods for adding and updating menu item
    categories. Returns statuses, or a Response
    of the getMenuCategories query."""
    if request.method == 'GET':
        return jsonify(getMenuCategories())
    elif request.method == 'POST':
        data = request.get_json()
        cats = None

        try:
            cats = data['categories']
        except (ValueError, KeyError):
            abort(400)

        addMenuCategories(list(map(lambda x: x[1], cats)))
        updateMenuCategoriesOrder(cats)
        return 'Added and updated', 201
    abort(400)
