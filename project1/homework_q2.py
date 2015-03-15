
"""
Update the quantity on two of the records, 
and then output all of the records from the table.
"""

#Import sqlite3
import sqlite3

#Connect to sqlite3 new.db
with sqlite3.connect("cars.db") as connection:
	#Grab cursor from database
	conn = connection.cursor()

	# Update the quantity of FORD S3 to 99 and quantity of Honda Classic to 44
	conn.execute("UPDATE invetory SET quantity = 99 WHERE model = 'S3'")
	conn.execute("UPDATE invetory SET quantity = 44 WHERE model = 'CLASSIC'")

	#Output all records
	rows = conn.execute("SELECT * FROM invetory").fetchall()
	for row in rows:
		print(row[0], row[1], row[2])

	conn.close()

