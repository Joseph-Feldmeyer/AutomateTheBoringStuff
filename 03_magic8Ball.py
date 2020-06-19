###################################################################
#File Name: 03_magic8Ball.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 19-06-2020

#Description: Return the fortune of user

###################################################################


import random 

def getAnswer(answerNumber): 
    if answerNumber == 1: 
        return 'It is certain' 
    elif answerNumber == 2: 
        return 'It is decidedly so' 
    elif answerNumber == 3: 
        return 'Yes' 
    elif answerNumber == 4: 
        return 'Reply hazy try again' 
    elif answerNumber == 5: 
        return 'It is decidedly so' 
    elif answerNumber == 6: 
        return 'Concentrate and ask again' 
    elif answerNumber == 7: 
        return 'My reply is no' 
    elif answerNumber == 8: 
        return 'Outlook not so good' 
    elif answerNumber == 9: 
        return 'Very doubtful' 

#r = random.randint(1,9) 
#fortune = getAnswer(r) 
#print(fortune) 

print(getAnswer(random.randint(1,9)))

