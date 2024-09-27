def divide_numbers(a, b):
    try:
        # Attempt to divide a by b
        result = a / b
    except ZeroDivisionError:
        # This block will handle the case where b is zero
        print("Error: Cannot divide by zero.")
        result = None
    except TypeError:
        # This block will handle the case where the inputs are not numbers
        print("Error: Invalid input type. Please provide numbers.")
        result = None
    else:
        # This block executes if no exception occurs
        print(f"Success: The result is {result}.")
    finally:
        # This block always executes, regardless of whether an exception occurred
        print("Execution complete.")
    
    return result

# Test cases
print(divide_numbers(10, 2))  # Successful division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, 'a'))  # Invalid input type
