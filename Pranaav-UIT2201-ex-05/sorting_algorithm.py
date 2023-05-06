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

    return (data, comparisons, swappings, start_time, end_time)


def selection_sort(data):

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

    return (data, comparisons, swappings, start_time, end_time)     

def insertion_sort(data):

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

    return (data, comparisons, swappings, start_time, end_time)


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


def printout_cases(random_lst, sorted_lst, comparisons, swappings, start, end):

    #print(f"Random list is : {random_lst}")
    print()

    #print(f"Sorted list is : {sorted_lst}")
    print("Size of data is : ",len(random_lst))
    print(f"Number of comparisons is : {comparisons}")
    print(f"Number of swappings is : {swappings}")
    #print(f"Starting time : {start}")
    #print(f"Ending time : {end}")
    print("Time taken is : ", end - start)
    print()

    print('-'*100)
    print()


def avg_scenario(random_lst):

    copy_1 = random_lst.copy()
    copy_2 = random_lst.copy()
    
    sorted_lst_sel, comparisons_sel, swappings_sel, start_sel, end_sel = selection_sort(copy_1)

    print("SELECTION SORT")
    printout_cases(copy_1,sorted_lst_sel, comparisons_sel, swappings_sel, start_sel, end_sel)

    sorted_lst_bub, comparisons_bub, swappings_bub, start_bub, end_bub = bubble_sort(copy_2)

    print("BUBBLE SORT")
    printout_cases(copy_2,sorted_lst_bub, comparisons_bub, swappings_bub, start_bub, end_bub)


def best_scenario(size):
    
    random_lst = [x for x in range(size)]

    copy_1 = random_lst.copy()
    copy_2 = random_lst.copy()

    sorted_lst_sel, comparisons_sel, swappings_sel, start_sel, end_sel = selection_sort(copy_1)

    print("SELECTION SORT")
    printout_cases(copy_1,sorted_lst_sel, comparisons_sel, swappings_sel, start_sel, end_sel)

    sorted_lst_bub, comparisons_bub, swappings_bub, start_bub, end_bub = bubble_sort(copy_2)

    print("BUBBLE SORT")
    printout_cases(copy_2,sorted_lst_bub, comparisons_bub, swappings_bub, start_bub, end_bub)


def worst_scenario(size):
    
    random_lst = [x for x in range(size,0,-1)]

    copy_1 = random_lst.copy()
    copy_2 = random_lst.copy()
    
    sorted_lst_sel, comparisons_sel, swappings_sel, start_sel, end_sel = selection_sort(copy_1)

    print("SELECTION SORT")
    printout_cases(copy_1,sorted_lst_sel, comparisons_sel, swappings_sel, start_sel, end_sel)

    sorted_lst_bub, comparisons_bub, swappings_bub, start_bub, end_bub = bubble_sort(copy_2)

    print("BUBBLE SORT")
    printout_cases(copy_2,sorted_lst_bub, comparisons_bub, swappings_bub, start_bub, end_bub)


def main_calc(user_input, second_user_input):

    result = user_input / (second_user_input * log2(second_user_input))

    return result


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    pass