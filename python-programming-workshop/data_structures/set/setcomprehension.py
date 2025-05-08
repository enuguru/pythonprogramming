
#set comprehensions and list comprehensions are basically the same, 
#but the former returns a set instead of a list:

setone = {x for x in [1, 1, 2, 3, 3, 1]}
print(setone)

#It's the same as:
#in the below code we specifically use the set function to create a set
settwo = set([i for i in [1, 1, 2, 3, 3, 1]])
print(settwo)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Generate a set of prime numbers up to 100 using set comprehension
primes = {x for x in range(2, 101) if is_prime(x)}
print(f"Prime numbers up to 100: {sorted(primes)}")
