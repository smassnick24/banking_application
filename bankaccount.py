# .py file used to declare the bank account class

class BankAccount:
    """Bank account class"""

    def __init__(self, name, account_number, routing_number, account_type, balance):
        self._name = name
        self._account_num = account_number
        self._routing_num = routing_number
        self._type = account_type
        self._bal = balance
        self._overdraw = -50
        self._interest = 1.001

    def __str__(self):
        return f"The Account of {self._name}.\nAccount #: {self._account_num}.\nRouting #: {self._routing_num}.\nBalance: {self._bal:.2f}\n"

    def __repr__(self):
        return f"Account: {self._account_num}"

    def get_name(self):
        return self._name

    def get_acnt(self):
        return self._account_num

    def get_route(self):
        return self._routing_num

    def get_type(self):
        return self._type

    def get_bal(self):
        return self._bal

    def deposit(self, num):
        """Deposit takes an integer or float and adds it to the current account balance"""
        if isinstance(num, int) or isinstance(num, float):
            self._bal += num
        else:
            raise ValueError("Input must be numberical")

    def withdraw(self, num):
        """Withdraw takes an int or float and removes it from the current balance
           if the withdraw would reduce the number to less than zero, state that 
           the balance is not sufficient for the withdrawal amount.
        """
        if isinstance(num, int) or isinstance(num, float):
            if self._bal - num < self._overdraw:
                return False
            else:
                self._bal -= num
        else:
            raise ValueError("Input must be numerical")

    def process_month(self):
        """process month takes the current balance of the account and multiplies it
           with the interest rate"""
        self._bal *= self._interest
