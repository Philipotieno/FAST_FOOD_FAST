from flask import Flask
from flask_restful import Api

import config

def create_app(config_name):
	'''creates the flask app depending on configurations passed'''
	app = Flask(__name__)
	api = Api(app)

	app.config.from_object(config.app_config)


	return app #retuns to the app after loading configurations