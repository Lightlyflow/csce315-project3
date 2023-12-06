from .querier import execute


def addImage(description: str, url: str, category: str, publicID: str):
    """Inserts an image into the database including which category it belongs to."""
    execute(f"INSERT INTO images (description, url, category, publicID) VALUES ('{description}', '{url}', '{category}', '{publicID}');")


def updateImage(imageID: int, description: str, category: str):
    """Only updates the images description and category by ID"""
    execute(f"UPDATE images SET description='{description}', category='{category}' WHERE id={imageID};")


def deleteImage(imageID: int):
    """Only deletes image from db."""
    execute(f"DELETE FROM images WHERE id={imageID};")


def getImages():
    """Retrieves all images from the database."""
    return execute(f"SELECT id, publicid, description, category, url FROM images;")
