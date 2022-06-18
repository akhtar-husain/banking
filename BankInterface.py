"""
Parent class/Interface for all banks.
"""
import abc
class Bank(metaclass=abc.ABCMeta):
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

    @classmethod
    def __subclasshook__(cls, subclass):
        return  (
            hasattr(subclass, "processPayment") and
            callable(subclass.processPayment) and
            hasattr(subclass, "processRefund") and
            callable(subclass.processRefund) or
            NotImplemented
        )

    @abc.abstractmethod
    def processPayment(self):
        """
        Implement this method to process payments.
        """
        return NotImplementedError

    @abc.abstractmethod
    def processRefund(self):
        """
        Implement this method to process refunds.
        """
        return NotImplementedError

    def pay(self):
        return self.processPayment()

    def refund(self):
        return self.processRefund()