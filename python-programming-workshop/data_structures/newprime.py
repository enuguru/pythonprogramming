# Initialize first two numbers of fibonacci sequence
fib = [0, 1]
# Create fibonacci sequence up to 2000
while True:
    next_num = fib[-1] + fib[-2]
    if next_num > 2000:
        break
    fib.append(next_num)
print(fib)
