import os
from psycopg2 import connect

def connect_to_db(config=None):
	'''func to connect to db'''
	if config == 'testing':
		db_name = os.getenv('TEST_DB')
	else:
		db_name = os.getenv('DB_NAME')

	host = os.getenv('DB_HOST')
	user = os.getenv('DB_USERNAME')
	password = os.getenv('DB_PASSWORD')


	return connect(
		database=db_name,
		host=host,
		user=user,
		password=password
		)

def create_users_table(cur):
	cur.execute(
		"""CREATE TABLE IF NOT EXISTS users(
		id serial PRIMARY KEY,
		username VARCHAR NOT NULL UNIQUE,
		email VARCHAR NOT NULL UNIQUE,
		password VARCHAR NOT NULL);""")

def create_orders_table(cur):
	cur.execute(
		"""CREATE TABLE IF NOT EXISTS orders(
		id serial,
		user_id INTEGER NOT NULL,
		meal VARCHAR NOT NULL,
		price INTEGER NOT NULl,
		ordered_at timestamp NOT NULL,
		modified_at timestamp NOT NULL);""")

def create_menu_table(cur):
	cur.execute(
		"""CREATE TABLE IF NOT EXISTS menu(
		id serial,
		order_id INTEGER,
		meal VARCHAR NOT NULL,
		price INTEGER NOT NULl,
		added_at timestamp NOT NULL,
		PRIMARY KEY (order_id)
		);""")

def main(config=None):
	conn = connect_to_db(config=config)
	conn.set_session(autocommit=True)
	cur = conn.cursor()

	create_users_table(cur)
	create_orders_table(cur)
	create_menu_table(cur)

	cur.close()
	conn.commit()
	conn.close()
	print('database created')

if __name__ == '__main__':
	main()
