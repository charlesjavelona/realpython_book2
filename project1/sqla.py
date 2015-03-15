# Create a SQLITE3 database and table


# Import the sqlite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# Get a cursor object used to execute SQL commands
cursor = conn.cursor()

# Create a table
"""
cursor.execute(""" CREATE TABLE invetory
					(make TEXT, model TEXT, 
					quantity INT)""")
"""

#Insert data
cursor.execute("INSERT INTO population"
				"VALUES('New York City', 'NY', 820000)")
cursor.execute("INSERT INTO population"
				"VALUES('San Francisco', 'CA', 800000)")

# Commit the changes
conn.commit()

# close the database connection
cursor.close()