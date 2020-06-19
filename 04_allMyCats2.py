###################################################################
#File Name: 04_allMyCats2.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 19-06-2020

#Description: 

###################################################################


catNames=[]

while True: 
    print('Enter the name of cat' + str(len(catNames) + 1) + '(Or enter nothing to stop.):') 
    name = input()
    if name == '': 
        break 
    catNames = catNames + [name]    # list concatenation

print('The cat names are:') 
for name in catNames: 
    print(' ' + name) 


