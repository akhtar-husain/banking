from BankInterface import Bank

class HdfcBank(Bank):
    """
    The parameter passed to this class' constructor will be received by the Bank interface. i.e. Parent class.
    """
    def processPayment(self):
        print(f"Your payment of amount {self.amount} for {self.account} has been processed by HDFC Bank.")

    def processRefund(self):
        print(f"Your refund of amount {self.amount} for {self.account} has been processed by HDFC Bank.")