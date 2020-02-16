'''
Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number
'''

def fibonacci_first(n): 
    if n<=0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return fibonacci_first(n-1) + fibonacci_first(n-2) 
  
# Driver Program 
 
print(fibonacci_first(5))