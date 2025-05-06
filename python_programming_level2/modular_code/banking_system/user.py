# user.py
from account import Account

class User:
    def __init__(self, name):
        self.name = name
        self.account = Account(self.name)

    def get_account(self):
        return self.account

    def __str__(self):
        return f"User: {self.name}"
