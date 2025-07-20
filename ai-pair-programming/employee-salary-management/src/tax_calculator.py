def calculate_tax(salary):
    if salary < 50000:
        return salary * 0.10
    else:
        return salary * 0.20

def net_pay(salary):
    return salary - calculate_tax(salary)