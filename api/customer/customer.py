from flask import Blueprint, render_template
from .customer_helper import getToppingNames

customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder = "static")


@customerBlueprint.route("/")
def home():
    toppingNames = getToppingNames()
    return render_template("customer_home.html", toppingNames=toppingNames)

