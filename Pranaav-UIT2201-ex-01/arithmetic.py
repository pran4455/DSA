# -*- coding: utf-8 -*-


"""

This module provides a series of functions that take in 3 numbers
as input and returns a boolean value based on whether any arithmetic
operation can be performed on them as the output. This is a part
of the exercises given under the course UIT2201 (Programming 
and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


#we check the addition operator
def sum_chk(a,b,c):

    """
    Function checks of addition operation is possible on
    given 3 numbers without changing their order. Output
    is given as a boolean [True if possible and False if
    not possible]. Input can be any number.

    The input numbers are not modified and there are no
    side effects.

    args:
        a: the first number.
        b: the second number.
        c: the third number.
    
    Returns:
        A boolean value based on whether addition is possible
        or not.

    """
    if a == (b+c):
        return True
    elif (a+b) == c:
        return True
    else:
        return False
#end of sum_chk function


#we check the subtraction operator    
def sub_chk(a,b,c):
    
    """
    Function checks of subtraction operation is possible on
    given 3 numbers without changing their order. Output
    is given as a boolean [True if possible and False if
    not possible]. Input can be any number.

    The input numbers are not modified and there are no
    side effects.

    args:
        a: the first number.
        b: the second number.
        c: the third number.
    
    Returns:
        A boolean value based on whether subtraction is possible
        or not.

    """

    if a == (b-c):
        return True
    elif (a-b) == c:
        return True
    else:
        return False
#end of sub_chk function


#we check the multiplication operator
def mul_chk(a,b,c):

    """
    Function checks of multiplication operation is possible
    on given 3 numbers without changing their order. Output
    is given as a boolean [True if possible and False if
    not possible]. Input can be any number.

    The input numbers are not modified and there are no
    side effects.

    args:
        a: the first number.
        b: the second number.
        c: the third number.
    
    Returns:
        A boolean value based on whether multiplication is
        possible or not.

    """

    if a == (b*c):
        return True
    elif (a*b) == c:
        return True
    else:
        return False
#end of mul_chk function


#we check the division operator
def div_chk(a,b,c):

    """
    Function checks of division operation is possible on
    given 3 numbers without changing their order. Output
    is given as a boolean [True if possible and False if
    not possible]. Input can be any number.

    The input numbers are not modified and there are no
    side effects.

    args:
        a: the first number.
        b: the second number.
        c: the third number.
    
    Returns:
        A boolean value based on whether division is possible
        or not.

    """

    if c!=0 and a == (b/c):
        return True
    elif b!=0 and (a/b) == c:
        return True
    else:
        return False
#end of div_chk function


#we check the power operator
def pow_chk(a,b,c):

    """
    Function checks of power operation is possible on
    given 3 numbers without changing their order. Output
    is given as a boolean [True if possible and False if
    not possible]. Input can be any number.

    The input numbers are not modified and there are no
    side effects.

    args:
        a: the first number.
        b: the second number.
        c: the third number.
    
    Returns:
        A boolean value based on whether power operation is
        possible or not.

    """

    if a == (b**c):
        return True
    elif (a**b) == c:
        return True
    else:
        return False
#end of pow_chk function

#function for checking whether 3 numbers satisfy any arithmetic equation
def arithmetic_chk(a,b,c):

    """
    This function takes in 3 numbers and checks whether any
    one of the arithmetic operations is possible on the given
    3 numbers. Input can be any number.

    The input is not modified in any way and there are no side
    effects.

    args:
        a: the first number.
        b: the second number.
        c: the third number.
    
    Returns:
        A boolean value based on whether any arithmetic operation
        is possible or not.

    """

    overall_answer = False  #initializing a variable for getting final answer
    
    if sum_chk(a,b,c):
        overall_answer = True
    if sub_chk(a,b,c):
        overall_answer = True
    if mul_chk(a,b,c):
        overall_answer = True
    if div_chk(a,b,c):
        overall_answer = True
    if pow_chk(a,b,c):
        overall_answer = True

    return overall_answer
#end of function arithmetic_chk


#driver code
if __name__ == "__main__":
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    a,b,c = 5,10,15  #issuing random numbers

    print("Value of a:",a,"\nValue of b:",b,"\nValue of c:",c)

    #stating whether any arithmetic operation can be performed
    print("Output of the function is:",arithmetic_chk(a,b,c))
    print()  #for spacing between lines

    a,b,c = -5,-2,10  #initializing negative values

    print("Value of a:",a,"\nValue of b:",b,"\nValue of c:",c)

    #stating whether any arithmetic operation can be performed
    print("Output of the function is:",arithmetic_chk(a,b,c))
    print()
    
    a,b,c = 7.7,2.2,3.5  #initializing float values
  
    print("Value of a:",a,"\nValue of b:",b,"\nValue of c:",c)

    #stating whether any arithmetic operation can be performed
    print("Output of the function is:",arithmetic_chk(a,b,c))
    print()

    a,b,c = 0,0,5  #initializing 0 for two variables

    print("Value of a:",a,"\nValue of b:",b,"\nValue of c:",c)

    #stating whether any arithmetic operation can be performed
    print("Output of the function is:",arithmetic_chk(a,b,c))
    print()
    
    a,b,c = 11,12,15  #initializing an impossible test case

    print("Value of a:",a,"\nValue of b:",b,"\nValue of c:",c)

    #stating whether any arithmetic operation can be performed
    print("Output of the function is:",arithmetic_chk(a,b,c))
    print()
    #end of code