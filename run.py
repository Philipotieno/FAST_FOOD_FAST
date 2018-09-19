import os

from app import create_app

config = os.getenv('APP_SETTINGS')
app = create_app(config)

if __name__ == '__main__':
	app.run(debug=True)