

def is_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

for i in range(1, 10000):
    if is_perfect_number(i):
        print(i)
