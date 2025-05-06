# new_user.py
from user import User

def create_new_user(name):
    user = User(name)
    account = user.get_account()
    account.deposit(500)
    account.check_balance()

create_new_user("Bob")
