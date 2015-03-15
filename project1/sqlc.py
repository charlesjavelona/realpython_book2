# Create a SQLITE3 database and table


# Import the sqlite3 library
import sqlite3
# Import the csv reader

# Create a new database if the database doesn't already exist
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#Open csv file and read 	
	employees = csv.reader(open("employees.csv", "rU"))

	#Create a new table called employees
	c.execute("CREATE TABLE employees" 
			"(firstname TEXT, lastname TEXT,"
				"ID INT)")
	#Input data to file
	c.executemany("INSERT INTO employees(firstname, lastname, ID)"
				 "VALUES(?, ?, ?)," employees)

# close the database connection
c.close()