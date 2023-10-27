from flask import Blueprint, render_template

menuboardBlueprint = Blueprint("menuboard", __name__, template_folder="templates")


@menuboardBlueprint.route("/")
def home():
    return render_template("menuboard.html")
