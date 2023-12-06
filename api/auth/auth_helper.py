from api.db import auth_querier
from .user import User

def getUserByEmail(email: str) -> User | None:
    """Returns User from their associated email if it exists"""
    if not userEmailExists(email):
        return None

    # If it does exist
    return User(email)

def userEmailExists(email: str) -> bool:
    """Checks if email exists in the database"""
    result = auth_querier.emailExists(email)
    return True if result is not None else False

def createUser(email: str) -> User:
    """Creates a user from given email. Returns sser object"""
    # Request to db
    auth_querier.addUser(email)

    return getUserByEmail(email)
