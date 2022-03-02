class Customer:
    def __init__(self, name, wallet_balance):
        self.name = name
        self.wallet_balance = wallet_balance

    def reduce_money_in_wallet(self, amount):
        total = self.wallet_balance - amount
        return total

    