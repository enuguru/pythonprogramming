def fibonacci(n):
    # Generate Fibonacci series using list comprehension
    fib = [0, 1]
    [fib.append(fib[i - 1] + fib[i - 2]) for i in range(2, n)]
    return fib[:n]


def main():
    """
    Main function to generate and display the Fibonacci series based on user input.

    The function prompts the user to input the number of terms they wish to display
    from the Fibonacci series. If the input is not a valid positive integer, an
    appropriate error message is shown. The function displays the Fibonacci series
    when the input is valid.

    Raises:
        ValueError: If the input provided by the user cannot be converted into an
        integer.
    """
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
