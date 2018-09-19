from flask import Flask, request
from flask_restful import Resource, reqparse

from app.api.v1.models import Order

class OrderResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('food')
	parser.add_argument('price')

	def post(self):
		'''method to post all orders'''
		args = OrderResource.parser.parse_args()
		food = args.get('food')
		price = args.get('price')

		order = Order(food=food, price=price)
		order = order.save()

		return {'message' : 'you have place your order', 'order':order}

	def get():
		'''method to get a food order'''
		pass

	def put():
		'''method to update agiven food order'''
		pass

	def delete():
		'''method to delete a given order'''
		pass
