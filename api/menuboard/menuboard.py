from flask import Flask, Blueprint, render_template
from .menuboard_helper import getMenuCategories, getToppingNames, getMenuData


menuboardBlueprint = Blueprint("menuboard", __name__, template_folder="templates", static_folder = "static")

@menuboardBlueprint.route("/", methods=['GET'])
def home():
    # Menu items dynamic loading
    menuQuery = getMenuData()
    menuCategories = getMenuCategories()
    
    print(menuCategories)
    menuItems = {category: [(item[0], item[2], item[3]) for item in menuQuery if item[1] == category] for category in menuCategories}

    numCategories = len(menuCategories)
    print(numCategories)
    numItems = 0
    for cat in menuItems:
        numItems += len(cat)
    numItems -= 15
    numCols = (numCategories//2)
    categorySize = str((450*numCols) // numCategories) + "%"
    itemSize = str((1350*numCols) // numItems) + "%"

    # Toppings
    toppingNames = getToppingNames()
    
    return render_template("menuboard.html", menuCategories=menuCategories, numCategories=numCategories, menuItems=menuItems, toppingNames=toppingNames, numCols=numCols, categorySize=categorySize, itemSize=itemSize)
