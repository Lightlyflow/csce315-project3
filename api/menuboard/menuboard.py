from flask import Blueprint, render_template
from .menuboard_helper import getMenuCategories, getMenuItems

menuboardBlueprint = Blueprint("menuboard", __name__, template_folder="templates")


@menuboardBlueprint.route("/")
def home():
    menuCategories = getMenuCategories()
    menuItems = {category: getMenuItems(category) for category in menuCategories}
    return render_template("menuboard.html")
