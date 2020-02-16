'''
Have the user enter a number and find all Prime Factors 
(if there are any) and display them.
'''


def is_prime(x):
    """
    Checks whether the given number x is prime or not
    """

    if x == 2:
        return True

    if x%2 == 0:
        return False

    for i in range(3,int(x**0.5)+1,2):
        if x%i == 0:
            return False

    return True


def gen_prime(current_prime):
    """
    Returns the next prime
    after the currentPrime
    """
    new_prime = current_prime + 1

    while True:
        if not is_prime(new_prime):
            new_prime += 1
        else:
            break
    
    return new_prime
    

def next_prime():

    current_prime = 2

    while True:
        next_prime_number = input("Insert 'n' to see the next prime number, insert 'q' to quit")
        if next_prime_number == 'n':
            print(current_prime)
            current_prime = gen_prime(current_prime)
        elif next_prime_number == 'q':
            print("This was the last prime number")
            break
        else:
            print("Please try again")
            continue

next_prime()