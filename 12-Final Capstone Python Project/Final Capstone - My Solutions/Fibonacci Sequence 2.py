'''
Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number
'''

  
def fibonacci_second(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
# Driver Program 
  
print(fibonacci_second(9)) 