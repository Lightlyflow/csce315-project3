from api.db import customer_querier
from flask_login import current_user
import os
import requests

def getMenuData():
    return customer_querier.getMenuItems()

def getMenuCategories(menuQuery) -> list():
    results = menuQuery
    categories = set()
    for result in results:
        categories.add(result[1])
    return list(categories)


def getToppingNames() -> list():
    results = customer_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping[0])
    return toppingNames

def placeOrder(menuItems):
    totalPrice = 0.0
    for menuItem in menuItems:
        menuItemPrice = 0.0
        itemName = menuItem['_name']

        toppingList = list()
        if menuItem['_topping1'] != 'null':
            toppingList.append(menuItem['_topping1'])
        if menuItem['_topping2'] != 'null':
            toppingList.append(menuItem['_topping2'])   
        if menuItem['_topping3'] != 'null':
            toppingList.append(menuItem['_topping3'])

        itemQuantity = int(menuItem['_quantity'])

        sweetness = menuItem['_sweetness']
        iceLevel = menuItem['_iceLevel']

        
        menuItemId = (customer_querier.getMenuItemId(itemName))[0][0]

        #Ingredients
        menuItemComponents = customer_querier.getMenuItemComponents(menuItemId)
        for component in menuItemComponents:
            currentInventory = (customer_querier.getIngredientQuantityInventory(component[0]))[0][0]
            newInventory = currentInventory - component[1] * itemQuantity
            customer_querier.setIngredientQuantityInventory(component[0], newInventory)

        #Cups and Straws
        currentInventory = customer_querier.getIngredientQuantityInventory(12)
        customer_querier.setIngredientQuantityInventory(12, currentInventory[0][0] - itemQuantity)
        currentInventory = customer_querier.getIngredientQuantityInventory(13)
        customer_querier.setIngredientQuantityInventory(13, currentInventory[0][0] - itemQuantity)

        #Toppings
        for topping in toppingList:
            toppingId = customer_querier.getToppingId(topping)[0][0]
            menuItemPrice += customer_querier.getToppingPrice(toppingId)[0][0]
            currentInventory = customer_querier.getIngredientQuantityInventory(toppingId)
            customer_querier.setIngredientQuantityInventory(toppingId, currentInventory[0][0] - itemQuantity)

        #Order Part
        totalPrice += menuItemPrice

        
        
    #Order
    orderId = customer_querier.getMaxOrderId()
    customer_querier.insertIntoOrderTable(orderId, totalPrice, current_user.email)




        


def getWeather():
    api_key = os.environ["WEATHER_API_KEY"]
    city_name = 'College Station'  
    #state_code = 'TX'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial'

    # Send a GET request to the API
    response = requests.get(url).json()
    return (int(response['main']['temp']), response['weather'][0]['description'])
