import unittest
import json

from . import create_up
from app.api.v1.models import db, User, Order

SIGN_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/signup'


class BaseClass(unittest.TestCase):
	'''Class for all test cases'''
	def setUP(self):
		#method creates a new test client and initializes a new database
		self.app = create_up(testing)
		self.client = self.app.test_client()
		self.app_context = self.app_context()
		self.app_context.push()
		self.user_data = { 
					"username" : "philioti",
					"email" : "philiotieb@gmail.com",
					"password" : "12wdrt56"
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
			username='mytestuser',
			email = 'mytestuser@gmail.com',
			password = 'testpassword'
			)
		self.test_user = User(
			username='tunchi',
			email = 'tunechir@gmail.com',
			password = 'test1234'
			)

	def logged_in(self):
		#User is first created
		self.client.post(SIGN_URL,
		data = json.dumps(self.user_data), content_type = 'apllication/json')

		#user can log in
		res = self.client.post(LOGIN_URL,
			data = json.dumps({"username" : "philioti", "password" : "12wdrt56"}), 
			content_type = 'apllication/json')

		return res

		def tearDown(self):
			'''Deletes the bd after test'''
			db.drop()