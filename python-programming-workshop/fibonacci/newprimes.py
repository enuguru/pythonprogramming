#write a program to find the prime numbers between 1 to 1000 using a class and using sieve of eratosthenes method
class PrimeFinder:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []

    def sieve_of_eratosthenes(self):
        # Initialize a boolean array of size limit+1 with True values
        is_prime = [True] * (self.limit + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        for number in range(2, int(self.limit**0.5) + 1):
            if is_prime[number]:
                for multiple in range(number * number, self.limit + 1, number):
                    is_prime[multiple] = False

        self.primes = [num for num, prime in enumerate(is_prime) if prime]

    def get_primes(self):
        return self.primes  
    def print_primes(self):
        for prime in self.primes:
            print(prime, end=' ')
        print()
# Create an instance of PrimeFinder with a limit of 1000
prime_finder = PrimeFinder(1000)

# Find prime numbers using the sieve of Eratosthenes method
prime_finder.sieve_of_eratosthenes()
# Print the prime numbers
prime_finder.print_primes()
