from functools import wraps
from flask import request
from app.api.v1.models import User

def token_required(func):
	'''checks validy of tokens'''
	@wraps(func)
	def decorated(*args, **kwargs):
		accsess_token = None
		try:
			authorization_header = request.headers.get('Authorization')
			if authorization_header:
				accsess_token = authorization_header.split(' ')[1]
			if accsess_token:
				user_id = User.decode_tokens(accsess_token)['id']
				return func(user_id, *args, **kwargs)
			return {'message' : 'you are not loged in/session expired'}, 401
		except Exception as e:
			return {'message' : 'an error occured'}
	return decorated