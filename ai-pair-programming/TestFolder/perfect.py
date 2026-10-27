# write a python program to print armstrong numbers till 10000
def is_armstrong(num):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return sum_of_powers == num
def print_armstrong_numbers(limit):
    armstrong_numbers = [num for num in range(limit + 1) if is_armstrong(num)]
    return armstrong_numbers
def main():
    limit = 10000
    armstrong_numbers = print_armstrong_numbers(limit)
    print(f"Armstrong numbers up to {limit}: {armstrong_numbers}")