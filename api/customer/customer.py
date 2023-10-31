from flask import Flask, Blueprint, render_template, url_for
from .customer_helper import getMenuCategories, getMenuItems, getToppingNames, getWeather


customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder = "static")


@customerBlueprint.route("/", methods=['GET'])
def home():
    menuCategories = getMenuCategories()
    toppingNames = getToppingNames()
    weather = getWeather()
    temperature = weather[0]
    conditions = weather[1]

    menuItems = {category: getMenuItems(category) for category in menuCategories}
    return render_template("customer_home.html", menuCategories=menuCategories, menuItems=menuItems, toppingNames=toppingNames, temperature=temperature, conditions=conditions)