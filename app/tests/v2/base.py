import json
from unittest import TestCase
from app.instance.createdb import connect_to_db
from instance.app import create_app

SIGNUP_URL = '/api/v2/user/signup'
LOGIN_URL = '/api/v2/user/login'

class BaseTestClass(TestCase):
    '''Base class with setup for tests'''
    def setUp(self):
        conn = connect_to_db('testing')
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS users CASCADE""" )
        cur.execute("""DROP TABLE IF EXISTS entries CASCADE""" )
        self.create_users_table(cur)
        self.create_entries_table(cur)
        
        self.app = create_app('testing')
        with self.app.app_context():
            from app.models import User, Order
        self.client = self.app.test_client()
        self.order_model = Order
        self.user_model = User
       
        self.user_data = {
                    "username":"philip", 
                    "email":"philip@gmail.com",
                    "password":"password"
                    }
        self.oder_data = {
                    "meal": "kuku",
                    "price": "100"
                    }
        self.first_user = User(
            username='testuser',
            email='testuser@email.com',
            password='password')

        self.first_order = Entry(
            meal='nyama',
            price ='200',
            user_id=1)

        self.test_user = User(
            username='apondi',
            email='stunya@mail.com',
            password='password')

    def logged_in_user(self):
        # first create user
        self.client.post(SIGNUP_URL,
        data = json.dumps(self.user_data), content_type = 'application/json')
        # then log in user
        res = self.client.post(LOGIN_URL,
        data=json.dumps({'username': 'philip', 'password': 'password'}),
        content_type='application/json')
        
        return res
    
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
        ordered_at timestamp NOT NULL,
        modified_at timestamp NOT NULL,
        PRIMARY KEY (user_id, id),
        FOREIGN KEY (user_id) REFERENCES users(id));""")

def create_menu_table(cur):
    cur.execute(
        """CREATE TABLE IF NOT EXISTS menu(
        id serial,
        meal_id INTEGER,
        meal VARCHAR NOT NULL,
        price INTEGER NOT NULl,
        added_at timestamp NOT NULL,
        PRIMARY KEY (meal_id, id),
        FOREIGN KEY (meal_id) REFERENCES users(id)
        );""")
    
    def tearDown(self):
        pass