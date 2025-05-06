# write a program to print prime numbers between 1 to 100 
def prime_numbers():
    for i in range(1,101):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i,end=' ')    
prime_numbers()