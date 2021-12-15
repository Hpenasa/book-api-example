import os
from os import error
import sqlite3
from sqlite3 import Error



def create_connection():
    conn = None

    try:
        database = os.getenv('DATABASE', '/app/sqlite.db')
        conn = sqlite3.connect(database)
    except Error as e:
            print("Error connection to DB: " + str(e))
    return conn