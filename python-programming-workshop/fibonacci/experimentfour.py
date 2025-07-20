# write a python program that prints the first 20 numbers in the fibonacci sequence

# def fibonacci(n):
def fibonacci(n):
    """
    Generate the first n numbers in the Fibonacci sequence.

    The Fibonacci sequence is defined as follows:
    - The first two numbers are 0 and 1.
    - Each subsequent number is the sum of the two preceding ones.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.
    """
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
def print_fibonacci(n):
    """
    Print the first n numbers in the Fibonacci sequence.

    This function generates the Fibonacci sequence up to the nth number
    and prints each number on a new line.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fib_sequence = fibonacci(n)
    for num in fib_sequence:
        print(num,end=" ")
if __name__ == "__main__":
    n = 20
    print_fibonacci(n)

