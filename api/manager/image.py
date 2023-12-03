from flask import Blueprint, request, render_template, abort, redirect, url_for

from .image_helper import imageUpload, imageDelete, imageUpdate

imageAPIBlueprint = Blueprint("images", __name__)


@imageAPIBlueprint.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("manager_images.html")
    elif request.method == 'POST':
        image = request.files['images']
        description = request.form.get("description")
        category = request.form.get("category")

        imageUpload(image, description, category)

        return redirect(url_for('images.upload'))

    abort(404)


@imageAPIBlueprint.route("/delete", methods=['POST'])
def delete():
    data = request.get_json()
    imageID = -1
    publicID = ""

    try:
        imageID = int(data['imageid'])
        publicID = data['publicid']
    except (ValueError, KeyError):
        abort(400)

    imageDelete(imageID, publicID)
    return "Deleted", 201


@imageAPIBlueprint.route("/update", methods=['POST'])
def update():
    data = request.get_json()
    imageID = -1
    description = ""
    category = ""

    try:
        imageID = int(data['imageid'])
        description = data['description']
        category = data['category']
    except (ValueError, KeyError):
        abort(400)

    imageUpdate(imageID, description, category)
    return "Updated", 201
