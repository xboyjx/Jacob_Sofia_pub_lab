import imp
from src.drinks import Drink

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_money_to_till(self, amount):
        total = self.till + amount
        return total

    def add_drink(self, drink_name, drink_price):
        self.drinks.append(Drink(drink_name, drink_price))