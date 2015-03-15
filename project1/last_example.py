from random import randint
import sqlite3


#with sqlite3.open("newnum.db") as connection:

#	conn = connection.cursor()
random_int = []
for _ in range(100):
	random = randint(0, 100)
	random_int.append(random)

print(random_int)