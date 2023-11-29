from flask import Flask, Blueprint, render_template
from .menuboard_helper import getMenuCategories, getToppingNames, getMenuData


menuboardBlueprint = Blueprint("menuboard", __name__, template_folder="templates", static_folder = "static")

@menuboardBlueprint.route("/", methods=['GET'])
def home():
    # Menu items dynamic loading
    menuQuery = getMenuData()
    menuCategories = getMenuCategories(menuQuery)
    # menuCategories.sort()
    for s in menuCategories:
        if s == "Seasonal":
            menuCategories.remove("Seasonal")
            menuCategories.insert(0,"Seasonal")
    
    print(menuCategories)
    menuItems = {category: [(item[0], item[2], item[3]) for item in menuQuery if item[1] == category] for category in menuCategories}

    numCategories = len(menuCategories)
    numItems = 0
    for cat in menuItems:
        numItems += len(cat)
    numItems -= 15
    numCols = (numCategories//2)+1
    categorySize = str((400*numCols) // numCategories) + "%"
    itemSize = str((1350*numCols) // numItems) + "%"

    # Toppings
    toppingNames = getToppingNames()
    
    return render_template("menuboard.html", menuCategories=menuCategories, menuItems=menuItems, toppingNames=toppingNames, numCols=numCols, categorySize=categorySize, itemSize=itemSize)
