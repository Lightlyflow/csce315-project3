import os
from typing import Any

import psycopg2

conn = psycopg2.connect(user=os.environ["DB_USERNAME"],
                        password=os.environ["DB_PASSWORD"],
                        host=os.environ["DB_HOST"],
                        database=os.environ["DB_DATABASE"])
DEBUG = os.environ["DEBUG"].lower() == "true"


def execute(query: str, getRet: bool = True) -> list[tuple[Any, ...]] | None:
    """Executes a query. Try not to query huge amounts of data.
    Set getRet to false if you are not getting values from the database."""
    with conn.cursor() as curs:
        try:
            print(query) if DEBUG else None
            curs.execute(query)
            conn.commit()
            return curs.fetchall() if getRet else None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == '__main__':
    result = execute("SELECT * FROM inventory_table LIMIT 10;")
    print(*result, sep="\n")
