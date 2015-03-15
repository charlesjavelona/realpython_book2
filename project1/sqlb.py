# Create a SQLITE3 database and table


# Import the sqlite3 library
import sqlite3


"""
#Insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 820000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
"""

# Insert multiple records using a tuple
cities = [
		('BOSTON', 'MA', 600000),
		('CHICAGO', 'CH', 270000),
		('Phoenix', 'AZ', 150000),
]

cursor.executemany('INSERT INTO population VALUES(?, ?, ?), cities')
"""
# Commit the changes
conn.commit()
"""

# close the database connection
cursor.close()