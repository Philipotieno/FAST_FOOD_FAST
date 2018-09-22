import json

from .base import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'

class Test_User(BaseClass):
	'''Test cases for users'''
	def test_signup(self):
		'''Test for rgistration of users'''
		response = self.client.post(SIGNUP_URL,
			data = json.dumps(self.user_data), content_type='application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], "succesfull registration")