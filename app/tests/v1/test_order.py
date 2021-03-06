import json

from .base import BaseClass
from app.api.v1.models import Order

POST_URL = '/api/v1/user/orders'
GET_ALL_URL = '/api/v1/user/orders'
GET_SINGLE_URL = '/api/v1/user/orders/1'

class Test_Order(BaseClass):
	'''Class to test for order test cases'''
	
	def test_post_order_not_loged_in(self):
		'''Cannot post orders without login'''
		response = self.client.post(POST_URL,
			data=json.dumps(self.order_data), content_type = 'application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 401)
		self.assertEqual(result['message'], 'you are not logged in/session expired')

	def test_get_order_without_loged_in(self):
		'''Cannot get a list of orders without login'''
		response = self.client.post(POST_URL,
			data=json.dumps(self.order_data), content_type = 'application/json')
		
		response = self.client.post(GET_SINGLE_URL,
			data = json.dumps(self.order_data), content_type = 'application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 401)
		self.assertEqual(result['message'], 'you are not logged in/session expired')

	def test_get_specific_order_without_loged_in(self):
		'''Cannot get a list of orders without login'''
		response = self.client.post(POST_URL,
			data=json.dumps(self.order_data), content_type = 'application/json')
		
		response = self.client.post(GET_ALL_URL,
			data = json.dumps(self.order_data), content_type = 'application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 401)
		self.assertEqual(result['message'], 'you are not logged in/session expired')
