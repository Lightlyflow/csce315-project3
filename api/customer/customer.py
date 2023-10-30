from flask import Blueprint, render_template
from .customer_helper import getMenuCategories, getMenuItems

customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder = "static")


@customerBlueprint.route("/")
def home():
    menuCategories = getMenuCategories()
    menuItems = {category: getMenuItems(category) for category in menuCategories}
    return render_template("customer_home.html", menuCategories=menuCategories, menuItems=menuItems)
