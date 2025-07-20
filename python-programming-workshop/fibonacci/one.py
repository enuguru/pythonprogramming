# create python program to find fibonacci series till n terms
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
print()  # for a newline after prime numbers
print(fibonacci(10))  # Example: print first 10 Fibonacci numbers
print()  # for a newline after prime
