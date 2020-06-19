###################################################################
#File Name: 04_myPets.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 19-06-2020

#Description: 

###################################################################


myPets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name: ') 
name = input()

if name not in myPets: 
    print('I do not have a pet named ' + name) 
else:
    print(name + ' is my pet.') 


