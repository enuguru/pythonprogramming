# Creating a tuple using a generator expression
numbers = (x for x in range(10) if x % 2 == 0)

# Converting the generator to a tuple
even_numbers_tuple = tuple(numbers)

print(even_numbers_tuple)
