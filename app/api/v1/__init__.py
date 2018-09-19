from flask import Flask
from flask_restful import Api

import instance.config

def create_app(config_name):
	'''creates the flask app depending on configurations passed'''
	app = Flask(__name__)
	api = Api(app)

	app.config.from_object(instance.config.app_config)

	from app.resources.users import RegisterUser, Login
	from app.resources.orders import OrderResource

	api.add_resource(RegisterUser, '/api/v1/user/signup')
	api.add_resource(Login, '/api/v1/user/login')


	return app #retuns to the app after loading configurations