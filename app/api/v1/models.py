from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import check_password_hash, generate_password_hash

class DATABASE():
	'''class for database'''
	def __init__(self):
		self.users = {}
		self.orders = {}
		self.all_users = 0
		self.all_orders = 0

	def drop(self):
		'''clears database after tests'''
		self.__init__()

db = DATABASE()

class Base():
    '''Base class to be inherited by User and Entry classes'''
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'modified', datetime.utcnow().isoformat())
        return self.view()

class User(Base):
	'''User model class'''
	def __init__(self, username, password, email):
		self.username = username
		self.email = email
		self.password = generate_password_hash(password)
		self.id = None
		self.created = datetime.utcnow().isoformat()
		self.modified = datetime.utcnow().isoformat()

	def view(self):
		'''View oject user in json format'''
		keys = ['username', 'email', 'id']
		return {key: getattr(self, key) for key in keys}

	def save(self):
		'''Save user information'''
		setattr(self, 'id', db.all_users + 1)
		db.users.update({self.id: self})
		db.all_users += 1
		db.orders.update({self.id: {}})
		return self.view()

	def password_validation(self, password):
		'''validate password'''
		if check_password_hash(self.password, password):
			return True
		return False

	def generate_token(self):
		'''method to generate tokens on user log in'''
		payload = {
		'exp' : datetime.utcnow()+timedelta(minutes=120),
		'iat' : datetime.utcnow(),
		'username': self.username,
		'id': self.id
		}
		token = jwt.encode(payload, str(current_app.config.get('SECRET')), algorithm = 'HS256')
		return token.decode()

	@staticmethod
	def decode_token(token):
		'''method to decode tokens after being generated'''
		payload = jwt.decode(token, str(current_app.config.get('SECRET')), algorithm = 'HS256')
		return payload

	@classmethod
	def get(cls, id):
		'''method to get user by id'''
		user = db.users.get(id)
		if user:
			return user
		return {'message' : 'User does not exist'}

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

class Order(Base):
	'''class to model order'''
	def __init__(self, food, quantity, user_id):
		self.food = food
		self.quantity = quantity
		self.id = None
		self.created = datetime.utcnow().isoformat()
		self.modified = datetime.utcnow().isoformat()
		self.user_id = user_id

	def save(self):
		'''method to fave food orders'''
		setattr(self, 'id', db.all_orders + 1)
		db.all_orders += 1
		db.orders[self.user_id].update({self.id: self})
		return self.view()

	def view(self):
		'''method to convert orders to json'''
		keys = ('id', 'food', 'quantity', 'user_id', 'created', 'modified')
		return {key: getattr(self, key) for key in keys}

	@classmethod
	def get(cls, user_id, id=None):
		'''method to get orders'''
		user_orders = db.orders.get(user_id)
		if not user_orders:
			return {'message':'No orders availiable'}
		if id:
			order = user_orders.get(id)
			if order:
				return order
			return {'message':'User does not have that order'}
		return user_orders