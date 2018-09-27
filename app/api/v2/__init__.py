from flask import Flask
from flask_restful import Api

import instance.config

def create_app(config_name):
	'''creates the flask app depending on configurations passed'''

	app  = Flask(__name__)
	api=Api(app)


	app.config.from_object(instance.config.app_config)

	with app.app_context():
		from app.api.v2.views.users import Signup


	api.add_resource(Signup, '/api/v2/user/signup')
		#api.add_resource(Login, '/api/v1/user/login')

	return app