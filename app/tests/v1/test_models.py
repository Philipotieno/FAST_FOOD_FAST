from .base import BaseClass
from app.api.v1.models import Order, User, db

class TestModels(BaseClass):
    '''models test cases'''
    def test_save_user(self):
    	'''Test if user adata is being saved'''
    	user = self.first_user.save()
    	self.assertEqual(1, len(db.users))
    	'''Assert if object is of the right class'''
    	self.assertTrue(isinstance(user, dict))

    def test_save_order(self):
    	'''test if order is placed and saved'''
    	self.first_user.save()
    	order = self.first_order.save()
    	self.assertEqual(1, len(db.orders[1]))
    	self.assertIsInstance(order, dict)

    def test_update_order(self):
    	self.first_user.save()
    	self.first_order.save()
    	order = Order.get(id=1, user_id=1)
    	data = {'food' :'kuku tamu', 'price' : '100'}
    	order = order.updates(data=data)
    	self.assertDictContainsSubset(data, order)

    def test_get_specific_order(self):
    	'''test to get order by id'''
    	self.first_user.save()
    	self.first_order.save()
    	order = Order.get(id=1, user_id=1)
    	self.assertTrue(isinstance(order, Order))

    def test_get_all_orders(self):
    	'''test if user can get all orders'''
    	self.first_user.save()
    	self.first_order.save()
    	order = Order.get(user_id=1)
    	self.assertTrue(isinstance(order, dict))
    	self.assertEqual(1, len(order))

    def test_nonexisting_order(self):
    	'''Test if user can get a non existing order'''
    	self.first_user.save()
    	order =Order.get(id=2, user_id=1)
    	self.assertEqual('No orders availiable', order['message'])