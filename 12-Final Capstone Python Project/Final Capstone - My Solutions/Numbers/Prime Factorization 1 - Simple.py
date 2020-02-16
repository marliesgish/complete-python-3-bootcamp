'''
Have the user enter a number and find all Prime Factors 
(if there are any) and display them.
'''

def primes(n):
    primes = [2]
    x = 3
    if n < 2:  # for the case of num = 0 or 1
        print(0)
        return
    while x <= n:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

n = input("Give us a number and we wil provide you with the prime numbers")
n = int(n)
primes(n)