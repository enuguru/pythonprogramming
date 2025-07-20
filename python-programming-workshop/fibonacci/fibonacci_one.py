
# print the armstrong numbers from 1 to 100
for num in range(1, 1001):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    if num == sum_of_powers:
        print(num, end=" ")
print()  # for a newline after Armstrong numbers


for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


