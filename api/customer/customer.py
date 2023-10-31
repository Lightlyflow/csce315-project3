from flask import Flask, Blueprint, render_template, url_for, request, jsonify
from .customer_helper import getMenuCategories, getMenuItems, getToppingNames, placeOrder


customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder = "static")


@customerBlueprint.route("/", methods=['GET'])
def home():
    menuCategories = getMenuCategories()
    toppingNames = getToppingNames()

    menuItems = {category: getMenuItems(category) for category in menuCategories}
    return render_template("customer_home.html", menuCategories=menuCategories, menuItems=menuItems, toppingNames=toppingNames)

@customerBlueprint.route("/post_endpoint", methods=['POST'])
def receive_saved_items():
    data = request.get_json()
    if 'savedItems' in data:
        saved_items = data['savedItems']
        placeOrder(saved_items)
        return jsonify({'message': 'Data received successfully'})
    
    return jsonify({'error': 'Invalid format'})
