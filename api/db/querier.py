import os
from typing import Any

from psycopg2 import connect, DatabaseError, extras, extensions


def getConnection():
    """
    Gets a connection to our Postgres database
    :return: A connection object to the database
    """
    return connect(user=os.environ["DB_USERNAME"],
                   password=os.environ["DB_PASSWORD"],
                   host=os.environ["DB_HOST"],
                   database=os.environ["DB_DATABASE"])


conn = None
DEBUG: bool = os.environ["DEBUG"].lower() == "true"


def execute(query: str, getRet: bool = True) -> list[tuple[Any, ...]] | None:
    """
    Queries the database to get some data (or not)
    :param query: Postgres query to execute
    :param getRet: If your query doesn't return anything, set this to True
    :return: List of tuples
    """
    global conn
    if conn is None or conn.closed:
        print("Re-establishing connection to database...")
        conn = getConnection()
        print("Re-established connection.")

    with conn.cursor(cursor_factory=extras.DictCursor) as curs:
        try:
            print(query) if DEBUG else None
            curs.execute(query)
            conn.commit()
            return curs.fetchall() if getRet else None
        except (Exception, DatabaseError) as error:
            print(error)


if __name__ == '__main__':
    result = execute("SELECT * FROM inventory_table LIMIT 10;")
    print(*result, sep="\n")
