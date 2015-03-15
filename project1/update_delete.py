#UPDATE and DELETE statements

import sqlite3

#Connect to database as connection:
with sqlite3.connect("new.db") as connection:
	#Grab cursor from database
	conn = connection.cursor()

	#Update database
	conn.execute("UPDATE population SET state = 'CHIc' WHERE city = 'CHICAGO'")

	#DELETE San Francisco
	conn.execute("DELETE FROM population WHERE city ='San Francisco'")

	print("\nNew Data:\n")
	
	#Execute command where it selects table population and fetches all rows
	rows = conn.execute("SELECT * FROM population").fetchall()

	for r in rows:
		print(r[0], r[1], r[2])