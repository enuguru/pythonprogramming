def handle_exceptions(a, b):
    try:
        # Potential exceptions can happen in these operations
        result = a / b
        print(f"The result of division is: {result}")

        # Example for potential KeyError
        my_dict = {'key1': 'value1'}
        print(my_dict['key2'])

    except ZeroDivisionError:
        # Handling division by zero
        print("Error: Division by zero is not allowed.")

    except KeyError as e:
        # Handling missing key in a dictionary
        print(f"Error: Missing key in dictionary - {e}.")

    except TypeError:
        # Handling incorrect type usage
        print("Error: Invalid type. Please provide numbers for division.")

    except Exception as e:
        # Generic exception handler for all other exceptions
        print(f"An unexpected error occurred: {e}")

    finally:
        # Code in this block always executes, whether an exception occurred or not
        print("Execution finished.")

# Test with various inputs
handle_exceptions(10, 0)       # ZeroDivisionError
handle_exceptions(10, 'a')     # TypeError
handle_exceptions(10, 2)       # KeyError inside the try block
handle_exceptions('x', 'y')    # TypeError
