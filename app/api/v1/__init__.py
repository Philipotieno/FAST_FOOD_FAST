from flask import Flask, render_template
from flask_restful import Api

import instance.config

def create_app(config_name):
	'''creates the flask app depending on configurations passed'''
	app = Flask(__name__)
	api = Api(app)

	app.config.from_object(instance.config.app_config)
	app.url_map.strict_slashes = False

	from app.views.users import RegisterUser, Login
	from app.views.orders import OrderResource

	api.add_resource(RegisterUser, '/api/v1/user/signup')
	api.add_resource(Login, '/api/v1/user/login')
	api.add_resource(OrderResource, '/api/v1/user/orders', '/api/v1/user/orders/<int:order_id>')

	@app.route("/")
	def home():
		return render_template('index.html')


	return app #retuns to the app after loading configurations