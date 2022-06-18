"""
Parent class for all banks.
"""
class Bank:
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

    def pay(self):
        return self.processPayment()

    def refund(self):
        return self.processRefund()