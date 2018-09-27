import json

from .base import BaseClass, SIGNUP_URL, LOGIN_URL

class Test_User(BaseClass):
    '''User test cases'''    

    def test_signup(self):
        """Test API can successfully register a new user (POST request)"""
        response = self.client.post(SIGNUP_URL,
            data = json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully registered")

    def test_login(self):
        """Test API can successfully log in registered users using username and password (POST request)"""
        self.test_user.add()
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'philip', 'password': 'password'}),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "You are successfully logged in")