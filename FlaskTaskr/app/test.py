import os
import unittest
import datetime

from views import app, db
from _config import basedir
from models import User, Task

TEST_DB = 'test.db'

class AllTests(unittest.TestCase):

	########################
	## Setup and Teardown ##
	########################


	# Executed prior to each test
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
												os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()


	#Executed after to each test
	def tearDown(self):
		db.drop_all()


	#Each test should start with 'test'
	def test_user_can_register(self):
		new_user = User('test_user', 
					"test@testmail.com", 
					"testing")
		db.session.add(new_user)
		db.session.commit()
		register_test = db.session.query(User).all()
		for test in register_test:
			test.name
		assert test.name == 'test_user'

	def test_form_is_present_on_login_page(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Please sign in to access your task list', response.data)

if __name__ == '__main__':
	unittest.main()


