from flask import Blueprint

menuAPIBlueprint = Blueprint("menu", __name__)


@menuAPIBlueprint.route("/menuitems", methods=['GET', 'POST'])
def menuItems():
    pass


@menuAPIBlueprint.route("/ingredient", methods=['GET', 'POST'])
def ingredients():
    pass
