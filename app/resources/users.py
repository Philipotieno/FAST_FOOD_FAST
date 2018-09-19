from flask import Flask
from flask_restful import Resource, reqparse

from app.models import User

class RegisterUser(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username')
	parser.add_argument('email')
	parser.add_argument('password')

	def post(self):
		'''methods=['POST']'''
		args = RegisterUser.parser.parse_args()
		username = args.get('username')
		email = args.get('email')
		password = args.get('password')

		username_exists = User.get_user_by_username(username=args['username'])
		email_exists = User.get_user_by_email(email=args['email'])

		if username_exists or email_exists:
			return {'message': 'User already exists'}, 203

		user = User(username=args.get('username'), email=args.get('email'), password=password)
		user = user.save()

		return {'message': 'succesfull registration', 'user': user}, 201