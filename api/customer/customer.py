from flask import Flask, Blueprint, render_template, url_for

customerBlueprint = Blueprint("customer", __name__, template_folder="templates", static_folder="static")


@customerBlueprint.route("/", methods=['GET'])
def home():
    return render_template("customer_home.html")
