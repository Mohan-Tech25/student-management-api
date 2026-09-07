from contextlib import contextmanager
from psycopg2 import pool
import os

from dotenv import load_dotenv


load_dotenv()


# ============================================================
# CONNECTION POOL
# ============================================================

connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,

    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


# ============================================================
# GET DATABASE CONNECTION
# ============================================================

@contextmanager#this decorator allows the function to be used in a with statement, ensuring that the connection is properly managed and returned to the pool after use.
def get_connection():

    connection = connection_pool.getconn()

    try:

        yield connection

    finally:

        connection_pool.putconn(connection)