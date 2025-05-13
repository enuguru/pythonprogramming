def sieve_of_eratosthenes(limit):
    """Generate all prime numbers up to the given limit using the Sieve of Eratosthenes."""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]

if __name__ == "__main__":
    limit = 1000
    prime_numbers = sieve_of_eratosthenes(limit)
    print("Prime numbers up to", limit, "are:")
    print(prime_numbers)