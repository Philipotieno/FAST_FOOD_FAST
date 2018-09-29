from flask import Flask, request
from flask_restful import Resource, reqparse

from app.api.v1.models import Order
from app.api.v1.decorator import token_required

class OrderResource(Resource):
	'''resources for user ordrs'''
	parser = reqparse.RequestParser()
	parser.add_argument('food', required=True, help='Food cannot be blank', type=str)
	parser.add_argument('quantity', required=True, help='quantity cannot be blank', type=int)

	@token_required
	def post(self, user_id):
		'''method to post all orders'''
		args = OrderResource.parser.parse_args()
		food = args.get('food', '')
		quantity = args.get('quantity', '')

		order = Order(food=food, user_id=user_id, quantity=quantity)
		order = order.save()

		return {'message' : 'you have place your order', 'order':order},201

	@token_required
	def get(self, user_id, order_id=None):
		'''method to get all food order and single food order'''
		user_order = Order.get(user_id=user_id, id=order_id)
		if isinstance(user_order, Order):
			return {'message':'Order found', 'order': user_order.view()}, 200

		if user_order.get('message'):
			return user_order, 404
		return {'message':'Your orders', 'orders': [user_order[order].view() for order in user_order]}

	@token_required
	def put(self, user_id, order_id):
		'''method to update agiven food order'''
		order = Order.get(user_id=user_id, id=order_id)
		if isinstance(order, dict):
			return order, 404 #No orders if user_id
		post_data = request.get_json()
		food = post_data.get('food', None)
		quantity =post_data.get('quantity', None) 
		data = {}
		if food:
			data.update({'food':food})
		if quantity:
			data.update({'quantity':quantity})

		order = order.updates(data=data)
		return {'message' : 'Order updated', 'New_order' : order}, 200