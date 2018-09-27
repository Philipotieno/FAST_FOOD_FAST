from .base import BaseClass

class Test_Models(BaseClass):
    '''Class for models test cases'''
    def test_can_create_user(self):
        '''Test successful user creation'''
        self.first_user.add()
        u = self.user_model.get('users', username=self.first_user.username)
        self.assertEqual(u[1], self.first_user.username)

    def test_can_create_order(self):
        '''Test successful entry creation'''
        self.user1.add()
        self.entry1.add()
        entry = self.order_model.get(user_id=1, entry_id=1)
        entry = self.order_model.order_dict(entry)
        self.assertEqual(order['price'], self.first_order.price)
        self.assertEqual(order['meal'], self.irst_order.meal)