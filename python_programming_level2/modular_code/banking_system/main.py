# main.py
from user import User

def main():
    # Create a new user
    user1 = User("Alice")

    # Get the user's bank account
    account = user1.get_account()

    # Perform some operations
    account.deposit(1000)
    account.check_balance()

    account.withdraw(250)
    account.check_balance()

    account.withdraw(1000)  # This will trigger an insufficient balance error
    account.check_balance()

if __name__ == "__main__":
    main()
