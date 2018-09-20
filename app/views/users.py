from flask import Flask
from flask_restful import Resource, reqparse

from app.api.v1.models import User

class RegisterUser(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
	parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
	parser.add_argument('password', required=True, help='Password cannot be blank', type=str)

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


class Login(Resource):
	'''Login resource'''
	parser = reqparse.RequestParser()
	parser.add_argument('username')
	parser.add_argument('password')

	def post(self):
		'''method for loging in'''
		args = Login.parser.parse_args()
		username = args['username']
		password = args['password']

		user = User.get_user_by_username(username)
		if not user:
			return {'message':'User not registered'}
		token = user.generate_token()
		return {'message' : 'You are now logged in', 'user':user.view(), 'token':token}, 200