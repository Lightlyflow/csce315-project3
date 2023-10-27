from flask import Blueprint, render_template

customerBlueprint = Blueprint("customer", __name__, template_folder="templates")


@customerBlueprint.route("/")
def home():
    return render_template("customer_home.html")
