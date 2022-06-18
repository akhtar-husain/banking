"""
Payment processing class.
"""
class Payment:
    def pay(self, processor):
        return processor.pay()

    def refund(self, processor):
        return processor.refund()