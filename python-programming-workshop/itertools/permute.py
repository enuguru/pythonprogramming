
import itertools

values = [1,2,3,4]

# Get all permutations of the three numbers.
result = itertools.combinations(values, 4)
for value in result:
    print(value)


result = itertools.permutations(values, 3)
for value in result:
    print(value)


result = itertools.combinations(values, 2)
for value in result:
    print(value)


result = itertools.permutations(values, 1)
for value in result:
    print(value)
