from api.db import auth_querier
from .user import User


def getUserByEmail(email: str) -> User | None:
    """
    Returns a User object if their email exists in the database.
    :param email: user email
    :return: User if exists, or None
    """
    if not userEmailExists(email):
        return None

    # If it does exist
    return User(email)


def userEmailExists(email: str) -> bool:
    """
    Checks if the user exists
    :param email: user email
    :return: True if email exists, else False
    """
    result = auth_querier.emailExists(email)
    return True if result is not None else False


def createUser(email: str) -> User:
    """
    Creates a user (not employee!) with given email
    :param email: user email
    :return: User object
    """
    # Request to db
    auth_querier.addUser(email)

    return getUserByEmail(email)
