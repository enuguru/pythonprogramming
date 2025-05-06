# write a python program to print perfect numbers till 10000 using a function
def is_perfect(n):
    # A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

for i in range(1, 10001):
    if is_perfect(i):
        print(i)
# output:
# 6
# 28
# 496  
# 8128