from api.db import customer_querier
import os
import requests


def getMenuCategories() -> list():
    results = customer_querier.getMenuItems()
    categories = set()
    for result in results:
        categories.add(result[1])
    return list(categories)

def getMenuItems(category) ->list():
    categories = customer_querier.getMenuItems()
    menuItems = []
    for cat in categories:
        if category == cat[1]:
            menuItems.append(cat[0])
    return menuItems
from api.db import customer_querier

def getToppingNames() -> list():
    results = customer_querier.getToppingNames()
    toppingNames = []
    for topping in results:
        toppingNames.append(topping)
    return toppingNames

def placeOrder(menuItems):
    for menuItem in menuItems:
        menuItemId = customer_querier.getMenuItemId(menuItem)
        menuItemComponents = customer_querier.getMenuItemComponents(menuItemId[0][0])
        for component in menuItemComponents:
            currentInventory = customer_querier.getIngredientQuantityInventory(component[0])
            newInventory = currentInventory[0][0] - component[1]
            customer_querier.setIngredientQuantityInventory(component[0], newInventory)

def getWeather():
    api_key = os.environ["WEATHER_API_KEY"]
    city_name = 'College Station'  
    #state_code = 'TX'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial'

    # Send a GET request to the API
    response = requests.get(url).json()
    return (int(response['main']['temp']), response['weather'][0]['description'])
