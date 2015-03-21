#CONTROLLER 

import os

#Grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = 'True'
SECRET_KEY = 'secret_key'

#Defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

