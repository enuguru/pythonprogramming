# account.py

class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.owner}'s account.")
        else:
            print("Deposit amount must be positive.")
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")
        return self.balance

    def check_balance(self):
        print(f"{self.owner}'s account balance: {self.balance}")
        return self.balance
