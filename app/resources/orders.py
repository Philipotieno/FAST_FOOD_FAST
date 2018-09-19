from flask import Flask, request
from flask_restful import Resource, reqparse

from app.api.v1.models import Order

class OrderResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('food')
	parser.add_argument('price')

	def post():
		'''method to post all orders'''
		pass

	def get():
		'''method to get a food order'''
		pass

	def put():
		'''method to update agiven food order'''
		pass

	def delete():
		'''method to delete a given order'''
		pass
