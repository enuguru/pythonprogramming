def is_perfect_number(num):
    """
    Determines whether a given number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper
    positive divisors, excluding itself. This function calculates the sum of all
    divisors of the specified number and checks if it matches the number.

    Arguments:
        num (int): The number to check for perfection. Must be a positive integer.

    Returns:
        bool: True if the number is perfect, otherwise False.
    """
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num


def generate_perfect_numbers(limit):
    """
    Generate a list of perfect numbers up to the specified limit.

    A perfect number is a positive integer that is equal to the sum
    of its proper divisors, excluding itself. This function iterates
    through all numbers from 1 to the given limit, checks if each
    number is perfect, and collects them into a list.

    Parameters:
        limit (int): The upper bound (inclusive) for finding perfect
            numbers. Must be a positive integer.

    Returns:
        list: A list of all perfect numbers found within the range
            from 1 to the specified limit.
    """
    perfect_numbers = []
    for num in range(1, limit + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers


# Generate perfect numbers up to 10000
limit = 10000
perfect_numbers = generate_perfect_numbers(limit)
print(f"Perfect numbers up to {limit}: {perfect_numbers}")
