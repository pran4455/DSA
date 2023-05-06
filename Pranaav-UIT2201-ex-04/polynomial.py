# -*- coding: utf-8 -*-


"""

This module provides a series of functions that calculate the
value of a polynomial, given the polynomial coefficient terms
and the value of x in 3 different time complexities, namely
O(n^2), O(nlogn) and O(n). This is a part of the exercises
given under the course UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 29 2023

Revised on Wed May 01 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


def complexity_n2(coefficients,x):

    '''
    The given function takes in the coefficients of a
    polynomial as well as the value of x to calculate
    the value of polynomial at a given x as well as
    number of operations taken.

    The input is not modified in any way and there
    are no side effects.

    args:
        coefficients: the coefficients of the polynomial
        x: the value of x to be substituted
    
    Returns:
        A tuple of polynomial value and number of
        operations performed.
    
    '''

    degree = len(coefficients) - 1
    total_sum = 0
    count = 0
    count += 2

    for coeff in coefficients:
        count += 1
        prod = 1
        for i in range(degree):
            count += 1
            prod *= x
        total_sum += prod*coeff
        degree -= 1
        count += 2

    return (total_sum, count)


def power(x, y):

    '''
    The given function calculates the value of x raised
    to the power y in time O(logn).

    The input is not modified in any way and there are no
    side effects.

    args:
        x: the base
        y: the power

    Returns:
        Value of x raised to the power y.
    
    '''

    global ct

    ct += 1

    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp


def complexity_nlogn(coefficients,x):

    '''
    The given function takes in the coefficients of a
    polynomial as well as the value of x to calculate
    the value of polynomial at a given x as well as
    number of operations taken. This implementation
    calculates value in O(nlogn) time.

    The input is not modified in any way and there
    are no side effects.

    args:
        coefficients: the coefficients of the polynomial
        x: the value of x to be substituted
    
    Returns:
        The polynomial value at given value x.
    
    '''
    
    global ct
    degree = len(coefficients) - 1
    total_sum = 0
    for coeff in coefficients:
        ct += 1
        prod = power(x,degree)
        total_sum += prod*coeff
        degree -= 1

    return total_sum


def horner_method(coefficients,x):

    '''
    The given function takes in the coefficients of a
    polynomial as well as the value of x to calculate
    the value of polynomial at a given x as well as
    number of operations taken. This is the implementation
    of horner method which calculates value in O(n) time.

    The input is not modified in any way and there
    are no side effects.

    args:
        coefficients: the coefficients of the polynomial
        x: the value of x to be substituted
    
    Returns:
        The polynomial value at given value x.
    
    '''

    global homer_ct

    result = coefficients[0]
    homer_ct += 1
    for i in range(1, len(coefficients)):
        homer_ct += 1
        result = result*x + coefficients[i]
    return result


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    ct = 0
    homer_ct = 0
    coeff = [x for x in range(1,11)]
    
    print(f"Coefficients of the polynomial being evaluated is: {coeff}")
    print()

    value, count = complexity_n2(coeff,2)
    print("Value of polynomial calculated by algorithm with O(n^2) time complexity: ",value)
    print("Number of comparisons is :",count)
    print()

    print("Value of polynomial calculated by lgorithm with O(nlogn) time complexity: ",complexity_nlogn(coeff,2))
    print("Number of comparisons is :",ct)
    print()

    print("Value of polynomial calculated by horner method: ",horner_method(coeff,2))
    print("Number of comparisons is :",homer_ct)
    print()
