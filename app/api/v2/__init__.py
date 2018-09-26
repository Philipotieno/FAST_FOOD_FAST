from flask import Flask

import instance.config

def create_app(config_name):
	'''creates the flask app depending on configurations passed'''

	app  = Flask(__name__)


	app.config.from_object(instance.config.app_config)


	return app