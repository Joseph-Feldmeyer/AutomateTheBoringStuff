###################################################################
#File Name: 02_exitExample.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 18-06-2020

#Description: 

###################################################################


import sys 

while True: 
    print('Type exit to exit.') 
    response = input()
    if response == 'exit': 
        sys.exit()
    print('You typed ' + response) 
