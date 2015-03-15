
"""
Using the “inventory” table from the previous homework assignment, 
add (INSERT) 5 records (rows of data) to the table. 
Make sure 3 of the vehicles are Fords while the other 2 are Hondas. 
Use any model and quantity for each.
"""

#Import sqlite3
import sqlite3

#Connect to sqlite3 new.db
with sqlite3.connect("cars.db") as connection:
	#Grab cursor from database
	conn = connection.cursor()

	#ADD(INSERT) 5 records of 3 Fords, 2 Hondas, make a tuple
	cars = [
			("FORD", "S5", 5),
			("FORD", "S4", 4),
			("FORD", "S3", 3),
			("HONDA", "CIVIC", 2),
			("HONDA", "CLASSIC", 1),
			]
	conn.executemany("INSERT INTO invetory VALUES(?, ?, ?)", cars)
	
	conn.close()
