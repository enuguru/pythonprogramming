# write a program to print prime numbers from 1 to 1000 using a function
def is_prime(n):
    # A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
for i in range(1, 1001):
    if is_prime(i):
        print(i,end=" " )    