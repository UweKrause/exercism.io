class BankAccount:

    def __init__(self):
        self.balance = 0
        self.status_open = False

    def get_balance(self):
        self.__is_open()
        return self.balance

    def open(self):
        self.__is_not_open()
        self.status_open = True
        self.balance = 0

    def deposit(self, amount):
        self.__is_open()

        if amount < 0:
            raise ValueError("cannot deposit negative")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.__is_open()

        if amount < 0:
            raise ValueError("cannot withdrwa negative")

        if amount > self.balance:
            raise ValueError("cannot withdraw more than deposited")

        self.balance -= amount
        return self.balance

    def close(self):
        self.__is_open()
        self.status_open = False

    def __is_open(self):
        if not self.status_open:
            raise ValueError("Account is not open")

    def __is_not_open(self):
        if self.status_open:
            raise ValueError("Account is open")
