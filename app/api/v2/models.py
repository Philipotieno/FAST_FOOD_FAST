import os
from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import check_password_hash, generate_password_hash
from psycopg2 import connect

from app.api.v2.db import connect_to_db

conn = connect_to_db(current_app.config.get('APP_SETTINGS'))
conn.set_session(autocommit=True)
cur = conn.cursor()


class Base():
    '''Base class to set up database'''

    def save(self):
        conn.commit()

    @staticmethod
    def get(table_name, **kwargs):
        '''pass condition as keyword argument, just one'''
        for key, val in kwargs.items():
            sql = "SELECT * FROM {} WHERE {}='{}'".format(table_name, key, val)
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def get_all(table_name):
        sql = 'SELECT * FROM {}'.format(table_name)
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @staticmethod
    def update(table, id, data):
        for key, val in data.items():
            string = "{}='{}'".format(key, val)
            sql = 'UPDATE {} SET {} WHERE id={}'.format(table, string, id)
            cur.execute(sql)
            conn.commit()

    @staticmethod
    def delete(table, id):
        sql = 'DELETE FROM {} WHERE id={}'.format(table, id)
        cur.execute(sql)
        conn.commit()

    def close(self):
        cur.close()
        conn.close() 

class User(Base):
    '''Class to model user'''
    def __init__(self, username, email, password):
        '''Initialize user variables'''
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    def add(self):
        cur.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (%s , %s, %s)
            """,
            (self.username, self.email, self.password))
        self.save()
    
    @staticmethod
    def user_dict(user):
        return dict(
            id=user[0],
            username=user[1],
            email=user[2]
        )
    @staticmethod
    def validate_password(password, username):
        user = User.get('users', username=username)
        if check_password_hash(user[3], password):
            return True
        return False

class Order(Base):
	pass