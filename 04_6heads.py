###################################################################
#File Name: 04_6heads.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 2020-11-04

#Description: Flip a coin 100 times. There is some change that 
#               the coin lands 6 heads in a row (or 6 tails in a 
#               row). Perform a simulation of 100 coin flips 
#               10,000 times, and find the probability of 
#               6 or more consecutive heads/tails. 

###################################################################

# Imports 
import random 

# Global Variables 
numberOfStreaks = 0 


# 10,000 times for loop 
for experimentNumber in range(10000): 
    # Code that creates 100 heads/tails values 
    
    # create empty list 
    coins = []
    # create streak counter 
    streak = 0
    # flip the coin 100 times 
    for flip in range(100): 
        coins.append(random.randint(0,1)) 

    # Check for streak 
    counter = 1 
    prevValue = None

    # iterate over list of coin flips 
    for i in coins: 
        if i == prevValue:          # If coin flip is same as prev, increment counter 
            counter += 1
        else: 
            if counter >= 6:        # if flip is differnet, check if 6 or more in row 
                streak += 1
            counter = 1
            prevValue = i 
    
    if streak >= 1: 
        numberOfStreaks += 1

print(numberOfStreaks) 
print('Chance of streak: %s%%' % (numberOfStreaks / 100))




