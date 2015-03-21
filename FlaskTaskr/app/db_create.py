import sqlite3

from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	#Get a cursor object use to execute SQL commands
	curr = connection.cursor()

	"""
	#Create a table 
	curr.execute("CREATE TABLE tasks(
					task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
					name TEXT NOT NULL, 
					due_date TEXT NOT NULL,
					priority INTEGER NOT NULL,
					status INTEGER NOT NULL)")
	"""
	#Insert dummy data into the table
	curr.execute("INSERT INTO tasks(name, due_date, priority, status)"
				"VALUES('Finish this tutorial', '02/03/2015', '10', '1')")

	curr.execute("INSERT INTO tasks(name, due_date, priority, status)"
				"VALUES('Fold clothes', '02/04/2015', '10', '1')")