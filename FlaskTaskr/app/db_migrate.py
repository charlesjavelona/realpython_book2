from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:

	#Get a cursor connection
	conn = connection.cursor()

	#Temporary change the name of tasks table
	conn.execute("""ALTER TABLE tasks RENAME TO old_tasks""")

	#Recreate a new tasks table with updated schema
	db.create_all()

	#Retrieve data from old_tasks table
	conn.execute("""SELECT name, due_date, priority, status FROM old_tasks ORDER BY task_id ASC""")

	#Save all rows as a list of tuples; set postnow and user_id to 1
	data = [(row[0], row[1], row[2], datetime.now(), '1') for row in conn.fetchall()]


	#Insert data into table tasks
	conn.executemany("""INSERT INTO tasks(name, due_date, priority, status, posted_date, user_id) VALUES (?, ?, ?, ?, ?, ?) """, data)

	#Delete old_tasks table
	conn.execute("DROP TABLE old_tasks")
