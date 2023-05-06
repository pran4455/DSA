# -*- coding: utf-8 -*-


"""

This module provides a function that takes in a list as an input
and returns a shuffled list as the output without using any inbuilt
functions. This is an implementation of the random module function
shuffle(data) using random module function randint(a,b). This is a
part of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import random  #we import random module for generating random integers within a given range


#this is a function for shuffling the list
def shuffle_list(data):

    """
    Shuffles the elements present in a list given as an argument
    input sequences is provided in the form of a list. The indices of 
    the elements must be defined. 
    
    If an empty list is given as the input, then the same empty list
    is returned as output.

    The input sequence will be modified into the shuffled list.

    args:
        data: an input sequence which needs to be shuffled
    
    Returns:
        A shuffled sequence

    """

    all_elem_same = True

    for i in data:  #checking if all the elements in list are same
        if i == data[0]:
            continue
        else:
            all_elem_same = False
            break
    
    if all_elem_same:  #returning the same sequence if all elements are same
        return data

    temp_list = data.copy()
    for i in range(len(data)):
        a=random.randint(i,len(data)-1)  #random index value generated from i since we have already iterated through previous indexes
        data[i],data[a]=data[a],data[i]  #interchanging index value with another value
    
    if temp_list!=data:  #ensuring that list is shuffled
        return data
    else:
        return shuffle_list(data)  #recursively calling until list is shuffled
#end of function shuffle_list


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
    #the following code will only be executed if the python file is run directly
    #code will be ignored if it is imported by another python source
    
    print("Output for list_generator(0):",list_generator(0))  #expected output is an empty list
    print("Output for list_generator(-10)):",list_generator(-10))  #since size is negative, empty list should be generated
    print("Output for list_generator(1):",list_generator(1))  #generates a list of size 1
    print()  #for spacing

    test_case = []  #empty list

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = list_generator(1)  #a list with only one element

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = list_generator(10,1,10)  #generating a list of 10 different elements

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = list_generator(10)  #generating a list of 10 different elements including negative numbers

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = list_generator(10,5,5)  #generating a list of 10 same elements

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = [x for x in range(10,0,-1)]  #generating a list of 10 different elements in descending order

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  #a list of characters

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()

    test_case = ["அரவிந்தன்", "அறவள்ளுவன்", "பாரதி", "ஔவையார்", "மணிமேகலை"]  #test case with tamil characters

    print("Test case is:",test_case)
    print("Shuffled list is:",shuffle_list(test_case))
    print()
    #end of code