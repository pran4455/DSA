# -*- coding: utf-8 -*-


"""

This module provides two functions that are used for implementing
merge sort. One of the functions is used for merging two sorted
lists and giving a third sorted list that combines the two lists
as output. Other function performs the merge sort by recursively
calling the first function and returns a sorted list. This is a
part of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 10 2023

Revised on Wed May 10 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

"""


import random
import time


def merge(A,B):

    '''
    This function merges two sorted lists, A and B, into a single
    sorted list C. It compares the elements from A and B one by one,
    placing the smaller element in C. The function keeps track of the
    number of comparisons made using the global variable count.

    The input lists A and B are not modified, and there are no side
    effects.

    Args:
        A: First sorted list.
        B: Second sorted list.

    Returns:
        A new list C containing all elements from A and B, merged in
        sorted order.

    '''

    global count

    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        count += 1
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i < len(A):
        C.extend(A[i:])
    else:
        C.extend(B[j:])
        
    return C


def merge_sort(data):

    '''
    This function implements the merge sort algorithm to sort a
    given list of data in ascending order. It recursively divides
    the list into smaller sublists, sorts them individually, and
    then merges them back together using the merge() function.

    The input list is not modified, and there are no side effects.

    Args:
        data: The list of elements to be sorted.

    Returns:
        A new list containing the sorted elements of the input list.

    '''

    n = len(data)
    if n < 2:
        return data[:]
    
    else:
        mid = n // 2

        return merge(merge_sort(data[:mid]), merge_sort(data[mid:]))


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


def worst_scenario(size):

    '''
    The function provides the parameters required for
    printing a worst case scenario for sorting.

    The input is not modified and there are no side effects.

    args:
        size: the size of random list to be generated
    
    Returns:
        None
    
    '''
    
    random_lst = [x for x in range(size,0,-1)]

    merge_sort(random_lst)

    print("Worst case scenario is:", count)


def best_scenario(size):

    '''
    The function provides the parameters required for
    printing a best case scenario for sorting.

    The input is not modified and there are no side effects.

    args:
        size: the size of random list to be generated
    
    Returns:
        None
    
    '''
    
    random_lst = [x for x in range(size)]

    merge_sort(random_lst)

    print("Best case scenario is:", count)


def avg_scenario(size):

    '''
    The function provides the parameters required for
    printing an average case scenario for sorting.

    The input is not modified and there are no side effects.

    args:
        size: the size of random list to be generated
    
    Returns:
        None
    
    '''

    random_lst = random_list(size)

    merge_sort(random_lst)

    print("Average case scenario is:", count)


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    count = 0

    random_lst = random_list(20)
    print(f"Random list is : {random_lst}")

    sorted_val = merge_sort(random_lst)
    print(f"Sorted list is: {sorted_val}")
    print(f"Count is : {count}")

    k = 10

    while k <= 10000:
        count = 0
        start = time.time()
        merge_sort(random_list(k))
        end = time.time()
        print(f"k is {k} and count is : {count}")
        print(f"Time taken is : {end - start}")
        print()
        k *= 10
    
    k = 20000
    count = 0
    start = time.time()
    merge_sort(random_list(k))
    end = time.time()
    print(f"k is {k} and count is : {count}")
    print(f"Time taken is : {end - start}")
    print()

    k = 50000
    count = 0
    start = time.time()
    merge_sort(random_list(k))
    end = time.time()
    print(f"k is {k} and count is : {count}")
    print(f"Time taken is : {end - start}")
    print()

    print("Test case size: 10000\n")
    count = 0

    avg_scenario(10000)

    count = 0

    best_scenario(10000)

    count = 0

    worst_scenario(10000)