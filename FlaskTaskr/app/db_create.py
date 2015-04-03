from views import db
from models import Task
from datetime import date

#Create the database and the db table
db.create_all()

#Insert dummy data - Task('Task summary', 'YYYY, MM, DD', 'Priority', '0 or 1' ) 
#db.session.add(Task("Finish this tutorial",
#		    date(2015, 3, 13), 10, 1))
#db.session.add(Task("Finish Real Python",
#		    date(2015, 4, 13), 10, 1))

#Commit the changes
db.session.commit()
