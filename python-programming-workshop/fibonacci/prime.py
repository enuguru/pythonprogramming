from memory_profiler import profile
import time

# write a python program to find prime numbers in a given range

@profile
def is_prime(num):
    """
    Determine whether a given number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@profile
def find_primes_in_range(range_start, range_end):
    """
    Find all prime numbers within a specified range.

    This function takes a start and end value and returns a list of all prime 
    numbers between the start (inclusive) and end (inclusive).

    Args:
        range_start (int): The starting value of the range (inclusive).
        range_end (int): The ending value of the range (inclusive).

    Returns:
        list: A list of integers representing the prime numbers within the range.
    """
    prime_numbers = []
    for current_number in range(range_start, range_end + 1):
        if is_prime(current_number):
            prime_numbers.append(current_number)
    return prime_numbers

# Timing the execution
start_time = time.time()
print(find_primes_in_range(10, 50))
end_time = time.time()

print(f"Execution time: {end_time - start_time:.6f} seconds")
