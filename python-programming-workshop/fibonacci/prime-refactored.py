# Refactored code to find prime numbers in a given range using a class

class PrimeFinder:
    """
    A class to find prime numbers and check primality.
    """

    @staticmethod
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

    def find_primes_in_range(self, range_start, range_end):
        """
        Find all prime numbers within a specified range.

        This method takes a start and end value and returns a list of all prime 
        numbers between the start (inclusive) and end (inclusive).

        Args:
            range_start (int): The starting value of the range (inclusive).
            range_end (int): The ending value of the range (inclusive).

        Returns:
            list: A list of integers representing the prime numbers within the range.
        """
        prime_numbers = []
        for current_number in range(range_start, range_end + 1):
            if self.is_prime(current_number):
                prime_numbers.append(current_number)
        return prime_numbers


# Example usage
if __name__ == "__main__":
    prime_finder = PrimeFinder()
    primes = prime_finder.find_primes_in_range(10, 50)
    print("Prime numbers between 10 and 50:", primes)