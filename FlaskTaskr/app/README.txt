So, we’ve split out our app into separate files, each with specific responsibilities:

	config.py: holds our app’s settings and configuration global variables


	views.py: contains the business logic - e.g., the routing rules - and sets up our Flask app (the latter of which could actually be moved to a different file)

	db_create.py: sets up and creates the database

	run.py: starts the Flask server

