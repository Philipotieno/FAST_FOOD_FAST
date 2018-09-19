from flask import current_app

class DATABASE():
	def __init__(self):
		self.users  = {}
		self.orders  = {}
		self.all_users  = 0
		self.all_orders  = 0

db = DATABASE()
# class Base():
# 	''''to be inherited by both users and orders class'''
# 	def latest(self, data):
# 		#validtae keys passing data
# 		for key in data:
# 			setattr(self, key)
# 		setatrr(self)
# 		return self.view

class User():
	'''User model class'''
	def __init__(self, username, password, email):
		self.username = username
		self.email = email
		self.password = password
		self.id = None

	def view(self):
		'''jsonify user object'''
		keys = ['username', 'email', 'id']
		return {key: getattr(self, key) for key in keys}

	def save(self):
		'''Save user information'''
		db.users.update({self.id: self})
		db.all_users += 1
		return self.view()

