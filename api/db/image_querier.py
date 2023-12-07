from .querier import execute


def addImage(description: str, url: str, category: str, publicID: str):
    """
    Inserts an image into the database including which category it belongs to.
    :param description: new description
    :param url: new image url
    :param category: new category
    :param publicID: new public ID
    :return: None
    """
    execute(f"INSERT INTO images (description, url, category, publicID) VALUES ('{description}', '{url}', '{category}', '{publicID}');")


def updateImage(imageID: int, description: str, category: str):
    """
    Only updates the images description and category by ID
    :param imageID: image ID
    :param description: new description
    :param category: new category
    :return: None
    """
    execute(f"UPDATE images SET description='{description}', category='{category}' WHERE id={imageID};")


def deleteImage(imageID: int):
    """
    Only deletes image from db, not from image CDN.
    :param imageID: image ID
    :return: None
    """
    execute(f"DELETE FROM images WHERE id={imageID};")


def getImages():
    """
    Retrieves all images from the database.
    :return: List containing id, public ID, description, category, and url
    """
    return execute(f"SELECT id, publicid, description, category, url FROM images;")
