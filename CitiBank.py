from BankInterface import Bank

class CitiBank(Bank):

    def processPayment(self):
        print(f"Your payment of amount {self.amount} for {self.account} has been processed by Citi Bank.")

    def processRefund(self):
        print(f"Your refund of amount {self.amount} for {self.account} has been processed by Citi Bank.")