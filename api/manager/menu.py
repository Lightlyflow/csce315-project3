from flask import Blueprint, request, jsonify, abort
from .menu_helper import getMenuItems, getIngredients

menuAPIBlueprint = Blueprint("menu", __name__)


@menuAPIBlueprint.route("/menuitems", methods=['GET', 'POST'])
def menuItems():
    if request.method == 'GET':
        return jsonify(getMenuItems())
    elif request.method == 'POST':
        abort(404)


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
        abort(404)
