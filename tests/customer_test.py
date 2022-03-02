import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Sofia", 20)

    def test_customer_has_name(self):
        self.assertEqual("Sofia", self.customer.name)


    def test_reduce_money_in_wallet(self):
        self.assertEqual(10.00, self.customer.reduce_money_in_wallet(10))

    def test_buy_drink(self):
        