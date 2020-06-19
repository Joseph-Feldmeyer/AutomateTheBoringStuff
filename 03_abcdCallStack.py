###################################################################
#File Name: 03_abcdCallStack.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 19-06-2020

#Description: 

###################################################################


def a(): 
    print('a() starts') 
    b()
    d()
    print('a() returns') 

def b(): 
    print('b() starts') 
    c()
    print('b() reuturns') 

def c(): 
    print('c() starts') 
    print('c() returns') 

def d(): 
    print('d() starts') 
    print('d() returns') 

a() 


