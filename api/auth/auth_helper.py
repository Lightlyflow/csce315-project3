from api.db import auth_querier
from .user import User


def getUserByEmail(email: str) -> User | None:
    # Request from db
    result = auth_querier.emailExists(email)[0]

    # If it doesn't exist
    if len(result) == 0:
        return None

    # If it does exist
    return User(email)


def createUser(email: str) -> User:
    # Request to db
    auth_querier.addUser(email)

    return getUserByEmail(email)
