from .base import BaseClass
from app.api.v1.models import Order, User, db

class TestModels(BaseClass):
	'''models test cases'''
	def test_save_user(self):
		'''Test if user adata is being saved'''
		user = self.first_user.save()
		self.assertTrue(isinstance(user, dict))

	def test_save_order(self):
		'''test if order is placed and saved'''
		self.first_user.save()
		self.first_order.save()
		order = self.first_order.save()
		self.assertIsInstance(order, dict)

	def test_get_all_orders(self):
		'''test if user can get all orders'''
		self.first_user.save()
		self.first_order.save()
		order = Order.get(user_id=1)
		self.assertIsInstance(order, dict)

	def tearDown(self):
		'''Deletes the db after test'''
		db.drop()