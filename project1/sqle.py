# Import the sqlite3 library
import sqlite3
# Import the csv reader
import csv


#Create a connecton object
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#Use fetchall() to retrieve all records from the query
	rows = c.execute("SELECT * FROM employees").fetchall()
	for r in rows:
		print(r[0], r[1])
# close the database connection
c.close()