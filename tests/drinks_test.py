import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennants", 4.00)

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(4.00, self.drink.price)