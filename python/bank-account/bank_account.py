import threading


class BankAccount:

    def __critical(func):
        """Decorator locks critical methods"""

        def _decorator(self, *args, **kwargs):
            self.lock.acquire()
            try:
                return func(self, *args, **kwargs)
            finally:
                self.lock.release()

        return _decorator

    def __init__(self):
        self.lock = threading.Lock()

        self.status_open = False

    @__critical
    def get_balance(self):
        self.__is_open()

        return self.balance

    @__critical
    def open(self):
        self.__is_not_open()

        self.status_open = True
        self.balance = 0

    @__critical
    def deposit(self, amount):
        self.__is_open()

        if amount < 0:
            raise ValueError("cannot deposit negative")

        self.balance += amount
        return self.balance

    @__critical
    def withdraw(self, amount):
        self.__is_open()

        if amount < 0:
            raise ValueError("cannot withdraw negative")

        if amount > self.balance:
            raise ValueError("cannot withdraw more than deposited")

        self.balance -= amount
        return self.balance

    @__critical
    def close(self):
        self.__is_open()

        self.status_open = False

    def __is_open(self):
        if not self.status_open:
            raise ValueError("Account is not open")

    def __is_not_open(self):
        if self.status_open:
            raise ValueError("Account is open")
