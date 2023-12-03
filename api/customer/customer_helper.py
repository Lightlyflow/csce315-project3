from api.db import customer_querier
from flask_login import current_user
import os
import requests

def getMenuData():
    return customer_querier.getMenuItems()

def getToppingData():
    return customer_querier.getToppingNames()

def getMenuCategories(menuQuery) -> list():
    results = menuQuery
    categories = set()
    for result in results:
        categories.add(result[1])
    return list(categories)


#Unused
def getToppingNames() -> list():
    results = customer_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames

def placeOrder(menuItems, orderDate):
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

        #Ingredients
        menuItemComponents = customer_querier.getMenuItemComponents(menuItemId)
        for component in menuItemComponents:
            customer_querier.subtractIngredientQuantityInventory(component[0], component[1] * itemQuantity)

        #Cups and Straws
        customer_querier.subtractIngredientQuantityInventory(12, itemQuantity)
        customer_querier.subtractIngredientQuantityInventory(13, itemQuantity)

        #Toppings
        toppingIdList = list()
        for topping in toppingList:
            toppingId = customer_querier.getToppingId(topping)[0][0]
            toppingIdList.append(toppingId)
            customer_querier.subtractIngredientQuantityInventory(toppingId, itemQuantity)
        for i in range (3 - len(toppingList)):
            toppingIdList.append(-1)

        #Order Part
        totalPrice += price * itemQuantity
        if iceLevel == 'Regular':
            iceLevelNum = 2
        elif iceLevel == 'Less':
            iceLevelNum = 1
        else:
            iceLevelNum = 0

        for i in range(itemQuantity):
            uniqueId = (customer_querier.getMaxUniqueId())[0][0] + 1
            customer_querier.insertIntoOrderPartTable(uniqueId, orderId, menuItemId, toppingIdList[0], toppingIdList[1], toppingIdList[2], round(price, 2), sweetness, iceLevelNum)


    #Order
    if (current_user.is_authenticated == True):
        currentEmail = current_user.email
    else:
        currentEmail = ''

    dateParts = orderDate.split('T')
    dateString = dateParts[0] + ' ' + dateParts[1] + ':00'
        
    customer_querier.insertIntoOrderTable(orderId, round(totalPrice, 2), currentEmail, dateString)

#def getPastOrders():
#    if (current_user.is_authenticated == True):
#        orderInfos = customer_querier.getOrderInfoForUser(current_user.email)
 #       for orderInfo in orderInfos:
 #           
 #   else:
 #       return []


def getWeather():
    api_key = os.environ["WEATHER_API_KEY"]
    city_name = 'College Station'  
    #state_code = 'TX'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial'

    # Send a GET request to the API
    response = requests.get(url).json()
    return (int(response['main']['temp']), response['weather'][0]['description'])
