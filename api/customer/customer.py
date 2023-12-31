from flask import Flask, Blueprint, render_template, url_for, request, jsonify
from .customer_helper import getMenuCategories, getToppingData, placeOrder, getWeather, getMenuData, getUserOrders, getCurrentTime
import os
customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder="static")


@customerBlueprint.route("/")
def home():
    """Renders the customer landing page."""
    googleID1 = os.environ.get('GOOGLE_CLIENT_ID')
    strings = "ID: " + googleID1
    print(strings)
    return render_template("customer_landing.html", googleID1=googleID1)


@customerBlueprint.route("/order", methods=['GET'])
def order():
    """Stores menu item, category, topping, time and user order data before rendering the customer home page."""
    # Menu items dynamic loading
    menuQuery = getMenuData()
    
    menuCategories = getMenuCategories()
    menuItems = {category: [(item[0], item[2], item[3], item[4]) for item in menuQuery if item[1] == category] for category in
                 menuCategories}
    # Weather api work to get temp and conditions
    weather = getWeather()
    temperature = weather[0]
    conditions = weather[1]

    # Toppings
    toppingNames = getToppingData()

    #Past Orders
    userOrders = getUserOrders()

    #Time
    currentTime = getCurrentTime()
    
    #counter
    counter = 0
    return render_template("customer_home.html", menuCategories=menuCategories, menuItems=menuItems, toppingNames=toppingNames, temperature=temperature, conditions=conditions, userOrders=userOrders, currentTime=currentTime, counter=counter)

@customerBlueprint.route("/post_endpoint", methods=['POST'])
def receive_saved_items():
    """Retrieves items that were previously saved in the cart."""
    data = request.get_json()
    if 'savedMenuItems' in data:
        savedItems = data['savedMenuItems']
        orderDate = data['orderDate']
        placeOrder(savedItems, orderDate)
        return jsonify({'message': 'Data received successfully'})

    return jsonify({'error': 'Invalid format'})
