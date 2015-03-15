# Create a SQLITE3 database and table


# Import the sqlite3 library
import sqlite3
# Import the csv reader
import csv

# Create a new database if the database doesn't already exist
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#Create database table
	#c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	#Open csv file and read 	
	employees = csv.reader(open("employees.csv", "rt"))

	#Input data to file
	c.executemany("INSERT INTO employees VALUES(?, ?)", employees)

# close the database connection
c.close()




