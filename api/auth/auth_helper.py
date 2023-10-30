from api.db import auth_querier
from .user import User


def getUserByEmail(email: str) -> User | None:
    # Request from db
    result = auth_querier.getUserByEmail(email)

    # If it doesn't exist
    if len(result) == 0:
        return None

    # If it does exist
    result = result[0]
    # TODO :: Check if manager
    return User(result[0], result[1], result[2], bool(result[3]))


def getUserById(user_id: str):
    # Request from db
    result = auth_querier.getUserById(int(user_id))

    # If it doesn't exist
    if len(result) == 0:
        return None

    # If it does exist
    result = result[0]
    # TODO :: Check if manager
    return User(result[0], result[1], result[2], bool(result[3]))


def createUser(email: str) -> User:
    # Request to db
    auth_querier.addUser(email)

    return getUserByEmail(email)
