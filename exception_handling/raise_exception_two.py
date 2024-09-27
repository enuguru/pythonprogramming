class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number error: {value} is not allowed!")

def calculate_square_root(x):
    if x < 0:
        # Throw (raise) a custom exception when a negative number is encountered
        raise NegativeNumberError(x)
    return x ** 0.5

try:
    result = calculate_square_root(-5)
except NegativeNumberError as e:
    print(f"Exception caught: {e}")
