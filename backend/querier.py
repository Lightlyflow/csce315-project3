import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(user=os.environ["DB_USERNAME"],
                        password=os.environ["DB_PASSWORD"],
                        host=os.environ["DB_HOST"],
                        database=os.environ["DB_DATABASE"])


def execute(query: str):
    """Executes a query. Try not to query huge amounts of data."""
    with conn.cursor() as curs:
        curs.execute(query)
        return curs.fetchall()


if __name__ == '__main__':
    result = execute("SELECT * FROM inventory_table LIMIT 10;")
    print(*result, sep="\n")
