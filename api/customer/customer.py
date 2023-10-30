from flask import Flask, Blueprint, render_template, url_for
from .customer_helper import getMenuCategories, getMenuItems

customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder = "static")


@customerBlueprint.route("/", methods=['GET'])
def home():
    menuCategories = getMenuCategories()
    menuItems = {category: getMenuItems(category) for category in menuCategories}
    return render_template("customer_home.html", menuCategories=menuCategories, menuItems=menuItems)
