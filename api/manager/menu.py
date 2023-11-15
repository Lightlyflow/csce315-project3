from flask import Blueprint, request, jsonify, abort
from .menu_helper import getMenuItems, getIngredients

menuAPIBlueprint = Blueprint("menu", __name__)


@menuAPIBlueprint.route("/menuitems", methods=['GET', 'POST'])
def menuItems():
    if request.method == 'GET':
        return jsonify(getMenuItems())
    elif request.method == 'POST':
        method = request.args.get("method", default="")
        data = request.get_json()

        if method == 'ADD':
            return 'ADD menu item'
        elif method == 'DEL':
            return jsonify('DEL items')
        elif method == 'UPDATE':
            pass
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
            pass
        elif method == 'DEL':
            pass
        elif method == 'UPDATE':
            pass
        abort(400)
