# Create a SQLITE3 database and table


# Import the sqlite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect("cars.db")

# Get a cursor object used to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute(""" CREATE TABLE invetory
					(make TEXT, model TEXT, 
					quantity INT)""")

# close the database connection
cursor.close()