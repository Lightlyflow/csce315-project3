from cloudinary import uploader
from werkzeug.datastructures import FileStorage

from api.db import image_querier

ALLOWED_EXTENSIONS = ["png", "jpg", "svg", "jpeg"]


def imageUpload(image: FileStorage, description: str | None, category: str | None) -> bool:
    """
    Attempts to upload an image to cloudinairy
    :param image: new image
    :param description: new description
    :param category: new category
    :return: True if the image can be uploaded, else False
    """
    description = "NULL" if description is None else description
    category = "NULL" if category is None else category

    if image and description and image.filename.split(".")[-1].lower() in ALLOWED_EXTENSIONS:
        upload_result = uploader.upload(image)
        image_querier.addImage(description, upload_result['secure_url'], category, upload_result['public_id'])
        return True
    return False


def imageUpdate(imageID: int, description: str | None, category: str | None):
    """
    Calls the querier to update an image entry in the database
    :param imageID: image ID
    :param description: new description
    :param category: new category
    :return: None
    """
    description = "NULL" if description is None else description
    category = "NULL" if category is None else category

    image_querier.updateImage(imageID, description, category)


def imageDelete(imageID: int, publicID: str):
    """
    Deletes image from database and image CDN. May take a few minutes to invalidate cached images.
    :param imageID: image ID
    :param publicID: public ID
    :return: None
    """
    image_querier.deleteImage(imageID)
    uploader.destroy(publicID)


def imageGet():
    """
    Calls the querier and returns the image from the database
    :return: List of images or [] if not found
    """
    result = image_querier.getImages()
    return result if result is not None else []
