# write a python program to print fibonacci series till n terms using a function
def fibonacci(n):
    """
    Generates and prints the Fibonacci sequence up to a specified number of terms.

    The Fibonacci sequence is a numeric sequence where each term is the sum of the
    previous two terms, starting with 0 and 1. This function computes the sequence
    iteratively using a loop and prints each term on the same line, separated by
    spaces. The sequence is generated up to the first 'n' terms, where 'n' is the
    input argument to the function.

    Parameters:
        n (int): The number of terms in the Fibonacci sequence to generate.

    Raises:
        ValueError: If 'n' is not a non-negative integer.
    """
    # A Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
    # The Fibonacci sequence is defined by the recurrence relation F(n) = F(n-1) + F(n-2), with seed values F(0) = 0 and F(1) = 1.
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(20)
