from flask import Flask, request
from flask_restful import Resource, reqparse

from app.api.v1.models import Order
from app.api.v1.decorator import token_required

class OrderResource(Resource):
	'''resources for user ordrs'''
	parser = reqparse.RequestParser()
	parser.add_argument('food', required=True, help='Food cannot be blank', type=str)
	parser.add_argument('price', required=True, help='Food cannot be blank', type=int)

	@token_required
	def post(self, user_id):
		'''method to post all orders'''
		args = OrderResource.parser.parse_args()
		food = args.get('food', '')
		price = args.get('price', '')

		order = Order(food=food, user_id=user_id, price=price)
		order = order.save()

		return {'message' : 'you have place your order', 'order':order},201

	def get(self, order_id=None):
		'''method to get all food order and single food order'''
		user_order = Order.get(id=order_id)
		if isinstance(user_order, Order):
			return {'message':'Order found', 'order': user_order.view()}, 200

		if user_order.get('message'):
			return user_order, 404
		return {'message':'Your orders', 'orders': [user_order[order].view()for order in user_order]}

	def put():
		'''method to update agiven food order'''
		pass

	def delete():
		'''method to delete a given order'''
		pass
