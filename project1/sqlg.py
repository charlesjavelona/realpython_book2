import sqlite3

#Connect to database as connection:
with sqlite3.connect("new.db") as connection:
	#Grab cursor from database
	conn = connection.cursor()

	#Create table called region, with city as text, and region as text
	#If it exists
	#conn.execute("""CREATE TABLE regions
	#				(city TEXT, region TEXT) 
	#			""")

	cities = [
			('New York City', 'Northeast'),
			('San Francisco', 'West'),
			('Chicago', 'Midwest'),
			('Houston', 'South'),
			('Phoenix', 'West'),
			('Boston', 'Northeast'),
			('Los Angeles', 'West'),
			('Houston', 'South'),
			('Philadelphia', 'Northeast'),
			('San Antonio', 'South'),
			('San Diego', 'West'),
			('Dallas', 'South'),
			('San Jose', 'West'),
			('Jacksonville', 'South'),
			('Indianapolis', 'Midwest'),
			('Austin', 'South'),
			('Detroit', 'Midwest'),
		]
	#INSERT cities
	conn.executemany("INSERT INTO regions VALUES(?, ?)", cities)

	#SELECT REGION AND SORT IT BY REGION IN ASCENDING ORDER
	rows = conn.execute("SELECT * FROM regions ORDER BY region ASC").fetchall()

	for row in rows:
			print(row[0], row[1])




