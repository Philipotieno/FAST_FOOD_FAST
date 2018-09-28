from .base import BaseClass

class Test_Models(BaseClass):
    '''Class for models test cases'''
    def test_can_create_user(self):
        '''Test successful user creation'''
        self.first_user.add()
        u = self.user_model.get('users', username=self.first_user.username)
        self.assertEqual(u[1], self.first_user.username)