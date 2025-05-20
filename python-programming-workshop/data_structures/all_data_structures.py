def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = []
for num in range(2, 201):
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers up to 200:")
print(prime_numbers)
