from flask import current_app

class DATABASE():
	def __init__(self):
		self.users  = {}
		self.orders  = {}
		self.all_users  = 0
		self.all_orders  = 0

db = DATABASE()

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
		setattr(self, 'id', db.all_users + 1)
		db.users.update({self.id: self})
		db.all_users += 1
		return self.view()

	@classmethod
	def get_user_by_email(cls, email):
		'''Method for getting user by email'''
		for idx in db.users:
			user = db.users.get(idx)
			if user.email == email:
				return user
		return None

	@classmethod
	def get_user_by_username(cls, username):
		'''Method for getting user by username'''
		for idx in db.users:
			user = db.users.get(idx)
			if user.username == username:
				return user
		return None

class Order():
	'''class to model order'''
	def __init__(self, food, price):
		self.food = food
		self.price =price
		self.id = None

	def save(self):
		'''method to fave food orders'''
		setattr(self, 'id', db.all_orders + 1)
		db.all_orders += 1
		return self.view()

	def view(self):
		'''method to convert orders to json'''
		keys = ('id', 'food', 'price')
		return {key: getattr(self, key) for key in keys}

	@classmethod
	def get(cls,id=None):
		'''method to get orders'''
		user_orders = db.orders.get(id)
		if not user_orders:
			return {'message':'No orders'}
		if id:
			order = user_orders.get(id)
			if order:
				return order
			return {'message':'User does not have an order'}
		return user_orders