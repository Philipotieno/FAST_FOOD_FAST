import unittest
import json

from app.api.v1 import create_app
from app.api.v1.models import User, Order, db

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'


class BaseClass(unittest.TestCase):
	'''Class for all test cases'''
	def setUp(self):
		#method creates a new test client and initializes a new database
		self.app = create_app('testing')
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.user_data = { 
					"username" : "philioti",
					"email" : "philiotieb@gmail.com",
					"password" : "password"
					}
		self.order_data = { 
					"food" : "nyama",
					"price" : "100"
					}

		self.first_user = User(
			username='mytestuser',
			email = 'mytestuser@gmail.com',
			password = 'testpassword'
			)
		self.first_order = Order(
					food ="mashakura",
					price ="200",
					user_id= 1
			)
		self.test_user = User(
			username='phillips',
			email = 'tunechir@gmail.com',
			password = 'test1234'
			)
		
	def tearDown(self):
		'''Deletes the db after test'''
		db.drop()