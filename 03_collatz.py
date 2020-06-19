###################################################################
#File Name: 03_collatz.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 19-06-2020

#Description: 
#   1. Define Collatz Sequence 
#       a. If number is even, print and reutrn nubmer // 2
#       b. If number is odd, print and return 3 * number + 1
#   2. User types number, and keep calling collatz() until return 1 

# Example: 3, 10, 5, 16, 8, 4, 2, 1 

###################################################################


def collatz(inputInteger): 
    
    # When 1
    if inputInteger == 1: 
        return
    # When even 
    elif inputInteger % 2 == 0: 
        newInteger = inputInteger // 2 
        print(newInteger) 
        collatz(newInteger) 
    # When odd
    else: 
        newInteger = (3 * inputInteger) + 1
        print(newInteger) 
        collatz(newInteger) 

print('Enter an integer: ') 
inputInteger = int(input())
collatz(inputInteger)

