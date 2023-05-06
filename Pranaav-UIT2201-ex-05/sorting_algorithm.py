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

Created on Wed Apr 03 2023

Revised on Wed May 03 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import random
import time
from math import log2


def bubble_sort(data):

    '''
    The given function sorts a given list using
    the bubble sort method and has a time complexity
    of O(n^2) and returns number of comparisons, swappings
    and amount of time taken to run the function inside
    a tuple.

    The given input is modified.

    args:
        data: the list to be sorted.

    Returns:
        A tuple containing sorted list number of comparisons,
        swappings and amount of time taken to run the function
        inside a tuple.
    
    '''

    comparisons = 0
    swappings = 0
    n = len(data)
    start_time = time.time()

    for i in range(n):
        comparisons += 1
        for j in range(n-i-1):
            comparisons += 1
            if data[j] > data[j+1]:
                swappings += 1
                data[j], data[j+1] = data[j+1], data[j]

    end_time = time.time()
    time_taken = end_time - start_time

    return (data, comparisons, swappings, time_taken)


def selection_sort(data):

    '''
    The given function sorts a given list using
    the selection sort method and has a time complexity
    of O(n^2) and returns number of comparisons, swappings
    and amount of time taken to run the function inside
    a tuple.

    The given input is modified.

    args:
        data: the list to be sorted.

    Returns:
        A tuple containing sorted list number of comparisons,
        swappings and amount of time taken to run the function
        inside a tuple.
    
    '''

    comparisons = 0
    swappings = 0
    n = len(data)
    start_time = time.time()

    for i in range(len(data)):

        comparisons += 1
        temp_ind = i

        for j in range(i+1, len(data)):
            comparisons += 1
            if data[temp_ind] > data[j]:
                temp_ind = j

        if i != temp_ind:
            swappings += 1
            data[i], data[temp_ind] = data[temp_ind], data[i]

    end_time = time.time()
    time_taken = end_time - start_time

    return (data, comparisons, swappings, time_taken)     


def insertion_sort(data):

    '''
    The given function sorts a given list using
    the insertion sort method and has a time complexity
    of O(n^2) and returns number of comparisons, swappings
    and amount of time taken to run the function inside
    a tuple.

    The given input is modified.

    args:
        data: the list to be sorted.

    Returns:
        A tuple containing sorted list number of comparisons,
        swappings and amount of time taken to run the function
        inside a tuple.
    
    '''

    comparisons = 0
    swappings = 0
    n = len(data)
    start_time = time.time()

    for i in range(1,n-1):

        j = i - 1
        temp_var = data[i]

        while j >= 0 and temp_var < data[j]:
                comparisons += 1
                swappings += 1
                data[j+1] = data[j]
                j-=1
        data[j+1] = temp_var

    end_time = time.time()
    time_taken = end_time - start_time

    return (data, comparisons, swappings, time_taken)


def random_list(size):

    '''
    The given function generates a random number of values
    and returns the values in a list.

    args:
        size: the number of point objects to be
        generated

    Returns:
        A list of random integer values.
    
    '''

    random_list = []

    for case in range(size):
        x_val = random.randint(-1000,1000)
        random_list.append(x_val)   

    return random_list  


def printout_cases(random_lst, sorted_lst, comparisons, swappings, time):

    '''
    This function provides a concise way of showing the
    original data, sorted data as well as number of
    comparisons, swappings and time taken.

    The input is not modified and there are no side effects.

    args:
        random_lst: the unsorted data
        sorted_lst: the sorted data
        comparisons: number of comparisons between the elements
        of the data
        swappings: number of swappings done
        time: time taken to run the function

    returns:
        None
    
    '''

    #print(f"Random list is : {random_lst}")
    print()

    #print(f"Sorted list is : {sorted_lst}")
    print("Size of data is : ",len(random_lst))
    print(f"Number of comparisons is : {comparisons}")
    print(f"Number of swappings is : {swappings}")
    print("Time taken is : ", time)
    print()

    print('-'*100)
    print()


def avg_scenario(size):

    '''
    The function provides the parameters required for
    printing an average case scenario for sorting.

    The input is not modified and there are no side effects.

    args:
        size: the size of random list to be generated
    
    returns:
        None
    
    '''

    random_lst = random_list(size)

    copy_1 = random_lst.copy()
    copy_2 = random_lst.copy()
    copy_3 = random_lst.copy()
    
    sorted_lst_sel, comparisons_sel, swappings_sel, time_sel = selection_sort(copy_1)

    print("SELECTION SORT")
    printout_cases(copy_1,sorted_lst_sel, comparisons_sel, swappings_sel, time_sel)

    sorted_lst_bub, comparisons_bub, swappings_bub, time_bub = bubble_sort(copy_2)

    print("BUBBLE SORT")
    printout_cases(copy_2,sorted_lst_bub, comparisons_bub, swappings_bub, time_bub)

    sorted_lst_ins, comparisons_ins, swappings_ins, time_ins = insertion_sort(copy_3)

    print("INSERTION SORT")
    printout_cases(copy_3,sorted_lst_ins, comparisons_ins, swappings_ins, time_ins)


def best_scenario(size):

    '''
    The function provides the parameters required for
    printing a best case scenario for sorting.

    The input is not modified and there are no side effects.

    args:
        size: the size of random list to be generated
    
    returns:
        None
    
    '''
    
    random_lst = [x for x in range(size)]

    copy_1 = random_lst.copy()
    copy_2 = random_lst.copy()
    copy_3 = random_lst.copy()

    sorted_lst_sel, comparisons_sel, swappings_sel, time_sel = selection_sort(copy_1)

    print("SELECTION SORT")
    printout_cases(copy_1,sorted_lst_sel, comparisons_sel, swappings_sel, time_sel)

    sorted_lst_bub, comparisons_bub, swappings_bub, time_bub = bubble_sort(copy_2)

    print("BUBBLE SORT")
    printout_cases(copy_2,sorted_lst_bub, comparisons_bub, swappings_bub, time_bub)

    sorted_lst_ins, comparisons_ins, swappings_ins, time_ins = insertion_sort(copy_3)

    print("INSERTION SORT")
    printout_cases(copy_3,sorted_lst_ins, comparisons_ins, swappings_ins, time_ins)


def worst_scenario(size):

    '''
    The function provides the parameters required for
    printing a worst case scenario for sorting.

    The input is not modified and there are no side effects.

    args:
        size: the size of random list to be generated
    
    returns:
        None
    
    '''
    
    random_lst = [x for x in range(size,0,-1)]

    copy_1 = random_lst.copy()
    copy_2 = random_lst.copy()
    copy_3 = random_lst.copy()
    
    sorted_lst_sel, comparisons_sel, swappings_sel, time_sel = selection_sort(copy_1)

    print("SELECTION SORT")
    printout_cases(copy_1,sorted_lst_sel, comparisons_sel, swappings_sel, time_sel)

    sorted_lst_bub, comparisons_bub, swappings_bub, time_bub = bubble_sort(copy_2)

    print("BUBBLE SORT")
    printout_cases(copy_2,sorted_lst_bub, comparisons_bub, swappings_bub, time_bub)

    sorted_lst_ins, comparisons_ins, swappings_ins, time_ins = insertion_sort(copy_3)

    print("INSERTION SORT")
    printout_cases(copy_3,sorted_lst_ins, comparisons_ins, swappings_ins, time_ins)


def main_calc(user_input, second_user_input):

    result = user_input / (second_user_input * log2(second_user_input))

    return result


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    for i in range(2,11):
        lst = random_list(i)
        copy_1 = lst.copy()
        copy_2 = lst.copy()
        copy_3 = lst.copy()

        sorted_lst_bub, comparisons_bub, swappings_bub, time_bub = bubble_sort(copy_1)
        sorted_lst_ins, comparisons_ins, swappings_ins, time_ins = insertion_sort(copy_2)
        sorted_lst_sel, comparisons_sel, swappings_sel, time_sel = selection_sort(copy_3)

        print("BUBBLE SORT")
        printout_cases(copy_1,sorted_lst_bub, comparisons_bub, swappings_bub, time_bub)
        print("INSERTION SORT")
        printout_cases(copy_2,sorted_lst_ins, comparisons_ins, swappings_ins, time_ins)
        print("SELECTION SORT")
        printout_cases(copy_3,sorted_lst_sel, comparisons_sel, swappings_sel, time_sel)

    print("Now testing their average case for large input size:")
    avg_scenario(10000)

    print("Now testing their best case for large input size:")
    best_scenario(10000)

    print("Now testing their worst case for large input size:")
    worst_scenario(10000)
