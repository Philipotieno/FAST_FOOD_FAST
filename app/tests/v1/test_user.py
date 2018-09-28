
import json

from .base import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'

class Test_User(BaseClass):
	'''Test cases for users'''
	def test_signup(self):
		'''Test for rgistration of users'''
		response = self.client.post(SIGNUP_URL,
			data=json.dumps(self.user_data), content_type='application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], "succesfull registration")
	
	def test_login(self):
		'''Test for log in of registered users'''
		self.test_user.save()
		response = self.client.post(LOGIN_URL,
			data=json.dumps({'username' : 'phillips', 'password' : 'test1234'}),
			content_type='application/json')
		self.assertEqual(response.status_code, 200)
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], "You are now logged in")
	
	def test_login_wrong_details(self):
		'''Test for log in of registered users with wrong details'''
		self.test_user.save()
		response = self.client.post(LOGIN_URL,
			data=json.dumps({'username' : 'philips', 'password' : 'test1234'}),
			content_type='application/json')
		self.assertEqual(response.status_code, 404)
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], "User not registered")

