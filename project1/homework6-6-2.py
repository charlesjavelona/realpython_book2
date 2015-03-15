import sqlite3

#Connect to database as connection:
with sqlite3.connect("cars.db") as connection:
	#Grab cursor from database
	conn = connection.cursor()

	#Add another table to accompany your “inventory” table called “orders”
	#conn.execute("""CREATE TABLE orders
	#			(make TEXT, model TEXT, order_date TEXT)""")

	cars = [
			("HONDA", "CIVIC", "1991 03 04"),
			("HONDA", "CIVIC", "1991 03 03"),
			("HONDA", "CIVIC", "1991 03 02"),
			("FORD", "S4", "1992 03 10"),
			("FORD", "S3", "1992 03 09"),
			("FORD", "S2", "1992 03 08"),
			("SUBARU", "IMPREZA", "1993 04 07"),
			("SUBARU", "X4", "1993 04 06"),
			("SUBARU", "X3", "1993 04 05"),
			("TOYOTA", "NISSAN", "1994 03 04"),
			("TOYOTA", "W2", "1994 03 03"),
			("TOYOTA", "W1", "1994 03 02"),
			("KIA", "SORENTO", "1995 02 01"),
			("KIA", "F5", "1995 02 10"),
			("KIA", "F4", "1995 02 09"),
			]
	#INSERT INTO orders
	conn.executemany("INSERT INTO orders VALUES(?, ?, ?)", cars)

	#SELECT ALL CARS THAT ARE DISTINCT IN MAKE MODEL AND ORDER DATE
	conn.execute("""SELECT DISTINCT orders.make, orders.model,
				orders.order_date, invetory.make FROM orders, invetory
				WHERE orders.model = invetory.model
				ORDER BY orders.make ASC """)

	rows = conn.fetchall()

	for row in rows:
		print(row[0], row[1], row[2])