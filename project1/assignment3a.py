"""
Create a new db called "newnum.db"
Add 100 random integers in the database
"""
import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    conn = connection.cursor()

    conn.execute("DROP TABLE if exists numbers")
    conn.execute("CREATE TABLE numbers(num int)")

    for num in range(100):
        conn.execute("INSERT INTO numbers VALUES(?)",
                    (random.randint(0, 100),))s
