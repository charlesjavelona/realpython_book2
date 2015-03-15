import sqlite3

with sqlite3.connect("new.db") as connection:
	conn = connection.cursor()

	#Retrieve data
	conn.execute("""SELECT DISTINCT population.city, population.poulation,
					regions.region FROM population, regions
					WHERE population.city = regions.city
					ORDER BY population.city ASC""")

	rows = conn.fetchall()

	for row in rows:
		print("City: " + row[0] + " Population: ", row[1],  "Region: " + row[2])



