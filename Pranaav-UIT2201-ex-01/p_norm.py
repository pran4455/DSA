# -*- coding: utf-8 -*-


"""

This module provides a function that takes in a sequence as an 
input and returns a float value as the output without using any
inbuilt functions. This is a part of the exercises given under
the course UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import random


#function for finding p-norm of a vector v
def norm(v,p=2):

    """
    The given function returns the p-norm value of a vector which 
    is the pth root of sum of each value in vector v to the pth power.
    It takes in the vector as a sequence of numbers with defined indices
    and the value of p. p has a default value of 2 for euclidean form.

    The function returns 'None' if an empty sequence is given as input.
    The function returns 'None' if value of p is given as 0 or less than 0.

    The input sequence is not modified and there are no side effects.

    args:
        v: represents the vector, takes input as a sequence of indexed objects.
        p: takes a default value of 2 for euclidean form, or takes in input
        in the form of a number.

    Returns:
        A floating point literal which is the p-norm of the input vector.
    
    """

    if not v:  #checking if vector is empty
        return None
    
    if p==0:  #checking if value of p is not 0
        return None
    
    pow_sum = 0  #initial value of total sum for pth power of elements in vector
    for i in v:
        pow_sum+=(i**p)
    return pow_sum**(1/p)  #taking the root of sum of powers to get p-norm
#end of norm function


#this is a function for generating a list of random numbers
def list_generator(size=1000,low=-10000,high=10000):

    """
    Create and return a list (of len 'size') containing random integers
    in the range from 'low' to 'high'. It requires the random module to
    generate random numbers using randint.

    args:
        size:  Length of the desired random list
        low:  The lower end of the range of numbers
        high:  The higher end of the range of numbers

    returns:
        A new list of given size containing random integers
        
    """
    
    random_list = []
    for count in range(size):
        random_list.append(random.randint(low, high))  #adding random elements to random_list
    return random_list
#end of function list_generator


#driver code
if __name__ == "__main__":
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    p = 0  #setting value of p=0
    v = list_generator(10)  #generating a random list of 10 elements

    print("Value of p is:",p,"\nValue of v is:",v)
    print("Output of norm(v,p):",norm(v,p))
    print()  #for spacing

    p = random.randint(-5,5)  #setting value of p to random number
    v = ()  #giving empty tuple as input

    print("Value of p is:",p,"\nValue of v is:",v)
    print("Output of norm(v,p):",norm(v,p))
    print()

    p = 0  #setting p to 0
    v = ()  #setting v to empty tuple

    print("Value of p is:",p,"\nValue of v is:",v)
    print("Output of norm(v,p):",norm(v,p))
    print()

    p = random.randint(-10,-1)  #setting a negative value for p
    v = tuple(list_generator(10))  #generating a random tuple of 10 elements

    print("Value of p is:",p,"\nValue of v is:",v)
    print("Output of norm(v,p):",norm(v,p))
    print()

    p = random.randint(1,10)  #setting value of p to random integer
    v = tuple(list_generator(10))  #generating a random tuple of 10 elements

    print("Value of p is:",p,"\nValue of v is:",v)
    print("Output of norm(v,p):",norm(v,p))
    print()

    p = random.random()  #setting value of p to random decimal value
    v = list_generator(10)  #generating a random list of 10 elements

    print("Value of p is:",p,"\nValue of v is:",v)
    print("Output of norm(v,p):",norm(v,p))
    print()

    v = tuple(list_generator(10))  #generating a random tuple of 10 elements

    print("Value of v is:",v)
    print("Output of norm(v) [euclidean norm]:",norm(v))
    print()
    #end of code