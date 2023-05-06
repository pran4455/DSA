# -*- coding: utf-8 -*-


"""

This module provides a function that takes in a list as an input
and returns a tuple containing length of input, its minimum and 
maximum value, along with number of comparisons as the output
without using any inbuilt functions. This is a part of the 
exercises given under the course UIT2201 (Programming and Data
Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 10 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import random


#this is the function for finding maximum and minimum value in a sequence
def minmax(data):

    """
    It finds the minimum and maximum value present in the given
    sequence of numbers along with the length of sequence as well
    as number of comparisons that occured in order to obtain the
    final results. The input sequence must have indices for the
    elements to be defined. Further, we assume that all elements
    in the sequence can be compared using standard Python operators.

    The input sequence may be empty, in which case, 'None' is returned.

    The original input is not modified and there are no side effects.

    args:
        data: a sequence of indexed objects that can be compared.

    Returns:
        A tuple containing lenght of sequence,minimum value,maximum
        value and number of comparisons.

    """
    
    if not data:  #ensuring that input is not an empty list
        return None

    minimum,maximum = data[0],data[0]  #setting initial values
    comparisons = 0
    length = 0
    
    for i in data:
        
        length+=1
        comparisons+=2 #there are two comparisons every iteration of the loop
        
        if i>maximum:  #checking if element is greater than current maximum value
            maximum = i  #if i is greater, then we update value of maximum
        elif i<minimum:  #checking if element is smaller than current minimum value
            minimum = i  #if i is smaller, then we update value of minimum
    
    return (length,minimum,maximum,comparisons)  #length of tuple will be number of iterations of for loop
#end of function minmax


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

    #stating how the order of output will be
    print("\nOutput will display in the order: Length of data, minimum value of data, "\
          "maximum value of data, number of comparisons\n")

    test_case = []  #empty list test case

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = ()  #empty tuple test case

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = [5]  #single element in a list

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = list_generator(10)  #generating a list of 10 elements including negative numbers

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = list_generator(10,1,10)  #generating a list of 10 positive elements upto 10

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = list_generator(10,5,5)  #generating a list of 10 same elements

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = tuple(list_generator(10))  #inputting a tuple of 10 random numbers

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  #a list of characters

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))
    print()

    test_case = {x for x in range(1,11)}  #generating a set of numbers between 1 and 10

    print("Test case is:",test_case)
    print("Output of function:",minmax(list(test_case)))  #set cannot be indexed, thus it needs to be converted into list
    print()

    test_case = ["அரவிந்தன்", "அறவள்ளுவன்", "பாரதி", "ஔவையார்", "மணிமேகலை"]  #test case with tamil characters

    print("Test case is:",test_case)
    print("Output of function:",minmax(test_case))  #set cannot be indexed, thus it needs to be converted into list
    print()
    
    #testing the program
    num_trials = random.randint(4, 10)
    for trials in range(num_trials):
        #determining size of list
        trial_size = random.randint(0, 10)

        #generating a list
        trial_list = list_generator(trial_size)

        #getting answer generated by minmax function
        if minmax(trial_list) == None:
            answer = None
        else:
            answer = (minmax(trial_list)[1],minmax(trial_list)[2])

        #checking the correct answer
        if trial_size == 0:
            right_answer = None
        else:
            right_answer = (min(trial_list),max(trial_list))

        print(answer,right_answer)
        
        if answer != right_answer:
            raise Exception("Function 'minmax' has returned wrong answer.")
    #end of code