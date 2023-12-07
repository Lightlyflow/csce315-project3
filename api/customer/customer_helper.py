from api.db import customer_querier
from flask_login import current_user
import os
import requests
import datetime


def getMenuData():
    """
    Grabs menu items from database.
    :return: 2D list of menu items
    """
    return customer_querier.getMenuItems()


def getToppingData():
    """
    Grabs topping names from database.
    :return: 2D list of topping names
    """
    return customer_querier.getToppingNames()


def getMenuCategories():
    """
    Returns all menu categories from the database.
    :return: 1D list of menu categories
    """
    results = customer_querier.getMenuCategories()
    categories = [item for sublist in results for item in sublist]
    return categories


def getCurrentTime():
    """
    Grabs the current time in %Y-%m-%dT%H:%M format.
    :return: current time
    """
    currentTime = datetime.datetime.now()
    formattedDatetime = currentTime.strftime("%Y-%m-%dT%H:%M")
    return formattedDatetime


def getUserOrders():
    """
    Retrieves orders for a specific user based on their associated email.
    :return: 2D list of user orders, or empty list if not logged in
    """
    if current_user.is_authenticated:
        results = customer_querier.getOrderInfoForUser(current_user.email)
        for result in results:
            result[1] = datetime.date(result[1].year, result[1].month, result[1].day)
            result[2] = "{:.2f}".format(result[2])
            result[7] = "{:.2f}".format(result[7])
            if result[9] == 2:
                result[9] = "Regular"
            elif result[9] == 1:
                result[9] = "Less"
            else:
                result[9] = "None"
        return results
    else:
        return []


# Unused
def getToppingNames() -> []:
    """
    Returns all topping names from the database.
    :return: 1D list of topping names
    """
    results = customer_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames


def placeOrder(menuItems, orderDate):
    """
    Executes the placing of an order. Updates order table and inventory.
    :param menuItems: List of menu items
    :param orderDate: Date order to be fulfilled
    :return: None
    """
    totalPrice = 0.0
    orderId = (customer_querier.getMaxOrderId())[0][0] + 1

    for menuItem in menuItems:
        itemName = menuItem['_name']

        toppingList = list()
        if menuItem['_topping1'] != 'null':
            toppingList.append(menuItem['_topping1'])
        if menuItem['_topping2'] != 'null':
            toppingList.append(menuItem['_topping2'])
        if menuItem['_topping3'] != 'null':
            toppingList.append(menuItem['_topping3'])

        itemQuantity = int(menuItem['_quantity'])

        print(orderDate)

        sweetness = menuItem['_sweetness']
        iceLevel = menuItem['_iceLevel']
        price = float(menuItem['_price'])

        menuItemId = (customer_querier.getMenuItemId(itemName))[0][0]

        # Ingredients
        menuItemComponents = customer_querier.getMenuItemComponents(menuItemId)
        for component in menuItemComponents:
            customer_querier.subtractIngredientQuantityInventory(component[0], component[1] * itemQuantity)

        # Cups and Straws
        customer_querier.subtractIngredientQuantityInventory(12, itemQuantity)
        customer_querier.subtractIngredientQuantityInventory(13, itemQuantity)

        # Toppings
        toppingIdList = list()
        for topping in toppingList:
            toppingId = customer_querier.getToppingId(topping)[0][0]
            toppingIdList.append(toppingId)
            customer_querier.subtractIngredientQuantityInventory(toppingId, itemQuantity)
        for i in range(3 - len(toppingList)):
            toppingIdList.append(-1)

        # Order Part
        totalPrice += price * itemQuantity
        if iceLevel == 'Regular':
            iceLevelNum = 2
        elif iceLevel == 'Less':
            iceLevelNum = 1
        else:
            iceLevelNum = 0

        for i in range(itemQuantity):
            uniqueId = (customer_querier.getMaxUniqueId())[0][0] + 1
            customer_querier.insertIntoOrderPartTable(uniqueId, orderId, menuItemId, toppingIdList[0], toppingIdList[1],
                                                      toppingIdList[2], round(price, 2), sweetness, iceLevelNum)

    # Order
    if current_user.is_authenticated:
        currentEmail = current_user.email
    else:
        currentEmail = ''

    if orderDate == "current":
        customer_querier.insertIntoOrderTableCurrent(orderId, round(totalPrice, 2), currentEmail, -1)
    else:
        dateParts = orderDate.split('T')
        dateString = dateParts[0] + ' ' + dateParts[1] + ':00'

        customer_querier.insertIntoOrderTable(orderId, round(totalPrice, 2), currentEmail, dateString)


# def getPastOrders():
#    if (current_user.is_authenticated == True):
#        orderInfos = customer_querier.getOrderInfoForUser(current_user.email)
#       for orderInfo in orderInfos:
#
#   else:
#       return []


def getWeather():
    """
    Retrieves the weather data for College Station from the OpenWeather API.
    :return: (temperature: int, description: str)
    """
    api_key = os.environ["WEATHER_API_KEY"]
    city_name = 'College Station'
    # state_code = 'TX'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial'

    # Send a GET request to the API
    response = requests.get(url).json()
    return int(response['main']['temp']), response['weather'][0]['description']
