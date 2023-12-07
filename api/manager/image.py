from flask import Blueprint, request, render_template, abort, redirect, url_for, jsonify

from .image_helper import imageUpload, imageDelete, imageUpdate, imageGet

imageAPIBlueprint = Blueprint("images", __name__)


@imageAPIBlueprint.route("/upload", methods=['GET', 'POST'])
def upload():
    """Sets up an endpoint for uploading images."""
    if request.method == 'GET':
        return render_template("manager_images.html")
    elif request.method == 'POST':
        image = request.files['image']
        description = request.form.get("description")
        category = request.form.get("category")

        imageUpload(image, description, category)

        return redirect(url_for('manager.images.upload'))

    abort(404)


@imageAPIBlueprint.route("/delete", methods=['POST'])
def delete():
    """Sets up an endpoint for deleting images."""
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
    """Sets up an endpoint for updating images."""
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


@imageAPIBlueprint.route("/get", methods=['GET'])
def get():
    """Sets up an endpoint to get the images. Returns
    a Response of the resulting query."""
    return jsonify(imageGet())
