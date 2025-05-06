# write a python program to print fibonacci series till n terms using a function
def fibonacci(n):
    # A Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
    # The Fibonacci sequence is defined by the recurrence relation F(n) = F(n-1) + F(n-2), with seed values F(0) = 0 and F(1) = 1.
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(20)
