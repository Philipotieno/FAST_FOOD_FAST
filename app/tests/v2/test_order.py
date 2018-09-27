import json

from .base import BaseClass

POST_URL = '/api/v1/user/orders'
GET_ALL_URL = '/api/v1/user/orders'
GET_SINGLE_URL = '/api/v1/user/orders/1'


class Test_Order_Case(BaseClass):
    '''Class for entry test cases'''
    def test_post_order(self):
        '''Test API can add entry made by logged in user'''
        response = self.logged_in_user()
        response = self.client.post(POST_URL,
            data = json.dumps(self.order_data), content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["message"], "Order has been published")