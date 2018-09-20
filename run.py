''''this is the entry point to fire up the app'''
import os

from app.api.v1 import create_app

config = os.getenv('APP_SETTINGS')
app = create_app(config)

if __name__ == '__main__':
	app.run(debug=True, port=5016)
