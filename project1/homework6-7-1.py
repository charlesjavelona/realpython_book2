import sqlite3

with sqlite3.connect("cars.db") as connection:
	conn = connection.cursor()

	sql = {'HONDA': 'SELECT COUNT(make) FROM orders WHERE model = "CIVIC"',
			'S4': 'SELECT COUNT(make) FROM orders WHERE model = "S4"',
			'S2': 'SELECT COUNT(make) FROM orders WHERE model = "S2"',
			'IMPREZA': 'SELECT COUNT(make) FROM orders WHERE model = "IMPREZA"',
			'X4': 'SELECT COUNT(make) FROM orders WHERE model = "X4"',
			'NISSAN': 'SELECT COUNT(make) FROM orders WHERE model = "NISSAN"',
			'W2': 'SELECT COUNT(make) FROM orders WHERE model = "W2"',
			'F5': 'SELECT COUNT(make) FROM orders WHERE model = "F5"', }

	for keys, values in sql.items():
		conn.execute(values)
		result = conn.fetchone()
		print(keys + ": ", result[0])


	#Show an example output
		#Make: Honda Model: Civic
		#Quantity: 99
		#Order count: 2
		


