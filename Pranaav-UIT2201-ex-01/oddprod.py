# -*- coding: utf-8 -*-


"""

This module provides a function that takes in a sequence as an
input and returns a list of pairs whose product is odd inside a
tuple as the output without using any inbuilt functions. This is
a part of the exercises given under the course UIT2201 (Programming 
and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 10 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import random


#creating a function for finding odd product pairs
def oddprod(input_sequence):

    """
    Returns a list of tuples of pairs of numbers whose product is odd as
    well as number of comparisons done in a tuple. It takes in input of a 
    sequence of numbers, and indices for the elements are expected to be
    defined. Any duplicate values [(3,7) and (7,3) are considered to be
    the same] will not be displayed.
    
    If an empty list is given as an input or if list contains only one element,
    then None is given out as output.

    The input sequence is not modified and there are no side effects.

    args:
        num_list=input sequence of indexed numbers

    Returns:
        A list of tuples which contains pair of numbers from input sequence
        whose product is an odd number and number of comparisons.

    """

    num_list = list(input_sequence)  #generating a list copy of input sequence

    count = 0  #represents the number of comparisons

    count+=1  #since we are checking if the size of list is greater than 1
    if len(num_list)<=1:  #checking if pair of numbers are possible
        return (None,count)  #if size is less than 2, then no pairs are possible
        
    pair = []  #gives the pair of numbers whose product is odd
    
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):  #i+1 will be first element because we do not need to check for any previous element
            count+=1
            if (num_list[i]*num_list[j])%2 != 0:  #checking if product is odd
                count+=1
                if num_list[i] != num_list[j]:  #ensuring that both elements are different
                    count+=1
                    if (num_list[i],num_list[j]) not in pair:
                        count+=1
                        if (num_list[j],num_list[i]) not in pair:
                            pair.append((num_list[i],num_list[j]))          
                elif num_list.count(num_list[i])>1:
                    count+=1
                    if (num_list[i],num_list[j]) not in pair:  #checking if there are duplicate
                        count+=1
                        if (num_list[j],num_list[i]) not in pair:
                            pair.append((num_list[i],num_list[j]))

    return (pair,count)
#end of function oddprod


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
        A new list of given size containing random integers.

    """
    
    random_list = []
    for count in range(size):
        random_list.append(random.randint(low, high))  #adding random elements to random_list
    return random_list
#end of function list_generator


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module
    
    test_case = []  #empty list

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()  #for spacing between lines

    test_case = [random.randint(-1000,1000)]  #a list with only a single element

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()

    test_case = list_generator(10)  #a randomly generated list of 10 elements including negative numbers

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()

    test_case = list_generator(10,1,10)  #a randomly generated list of 10 elements with only positive numbers upto 10

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()

    test_case = list_generator(10,5,5)  #a list of 10 elements of same value

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()
    
    test_case = tuple(list_generator(10))  #inputting a tuple value into function

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()

    test_case = set(list_generator(10))  #inputting a set value into function

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()

    test_case = [4 ,5 ,5 ,3 ,4 ,5 ,3 ,7 ,3 ,5]  #inputting duplicate values in unordered form

    print("Test case is:",test_case)
    print("Odd product pairs:",oddprod(test_case)[0])
    print("Number of comparisons:",oddprod(test_case)[1])
    print()
    #end of code 