#CONTROLLER 

import os

#Grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = 'True'
SECRET_KEY = 'secret_key'

#Defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

#Database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
