# write a python program to find primes numbers in a range
def is_prime(n):
    if n < 2:
        return False
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True
for i in range(1, 100):
    if is_prime(i):
        print(i,end=" ")

