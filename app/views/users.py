from flask import Flask
from flask_restful import Resource, reqparse
import re

from app.api.v1.models import User
from app.api.v1.decorator import no_input

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

        email_format = re.compile(
        r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)")
        username_format = re.compile(r"(^[A-Za-z]+$)")

        if not (re.match(username_format, username)):
            return {'message' : 'Invalid username'}, 400
        elif not (re.match(email_format, email)):
            return {'message': 'Invalid email. Ensure email is of the form example@mail.com'}, 400
        if len(username) < 4:
            return {'message' : 'Username should be atleast 4 characters'}, 400
        if no_input(username) or no_input(email) or no_input(password):
			return {'message':'Fill all the fields'}, 400

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

		if no_input(username) or no_input(password):
			return {'message':'Fill all the fields'}, 400

		user = User.get_user_by_username(username)
		if not user:
			return {'message':'User not registered'}, 404
		token = user.generate_token()
		return {'message' : 'You are now logged in', 'user':user.view(), 'token':token}, 200