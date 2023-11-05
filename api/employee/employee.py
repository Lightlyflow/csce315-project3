from flask import Flask, Blueprint, render_template, url_for, request, jsonify
from .employee_helper import getMenuCategories, getToppingNames, placeOrder, getWeather, getMenuData
employeeBlueprint = Blueprint("employee", __name__, template_folder="templates", static_folder = "static")


@employeeBlueprint.route("/", methods=['GET'])
def home():
    # Menu items dynamic loading
    menuQuery = getMenuData()
    menuCategories = getMenuCategories(menuQuery)
    #print(menuCategories)
    menuItems = {category: [(item[0], item[2]) for item in menuQuery if item[1] == category] for category in menuCategories}

    # Weather api work to get temp and conditions
    weather = getWeather()
    temperature = weather[0]
    conditions = weather[1]

    # Toppings
    toppingNames = getToppingNames()
    
    return render_template("employee_home.html", menuCategories=menuCategories, menuItems=menuItems, toppingNames=toppingNames, temperature=temperature, conditions=conditions)

@employeeBlueprint.route("/post_endpoint", methods=['POST'])
def receive_saved_items():
    data = request.get_json()
    if 'savedItems' in data:
        saved_items = data['savedItems']
        placeOrder(saved_items)
        return jsonify({'message': 'Data received successfully'})
    
    return jsonify({'error': 'Invalid format'})
