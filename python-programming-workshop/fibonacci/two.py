# write a python program to find fibonacci series till n terms
def fibonacci(n):
    fib = [0, 1]
    [fib.append(fib[i - 1] + fib[i - 2]) for i in range(2, n)]
    return fib[:n]
def main():
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive number")
            return

        result = fibonacci(n)
        print(f"\nFibonacci series with {n} terms:")
        print(result)

    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
