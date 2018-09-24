import os

from app.api.v1 import create_app

config = os.getenv('APP_SETTING')
app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True, port=5006)
    