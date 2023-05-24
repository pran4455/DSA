# -*- coding: utf-8 -*-


"""

This module provides two functions that are used for implementing
quick sort. One of the functions is used for merging two sorted
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


def partition(data,i,j,pivot):


    '''
    This function partitions a given list 'data' based on a pivot
    element. It rearranges the elements in the list such that all
    elements smaller than the pivot are placed to the left of it,
    and all elements greater than the pivot are placed to the right
    of it.

    The input list 'data' is modified during the partitioning
    process.

    Args:
        data: The list of elements to be partitioned.
        i: The starting index of the partitioning range.
        j: The ending index of the partitioning range.
        pivot: The pivot element used for partitioning.

    Returns:
        The index of the pivot element after partitioning.
    
    '''

    global count
     
    while True:
        count += 1
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        
        if i>=j:
            break

        data[i] , data[j] = data[j] , data[i]
        j -= 1
        i += 1

    data[i] , data[len(data)-1] = data[len(data)-1] , data[i]
    return i


def getmid_index(arr, left, right):

    '''
    This function determines the index of the middle element
    in a given list 'arr' between the indices 'left' and 'right'.
    It considers three elements: the element at the 'left' index,
    the element at the 'right' index, and the element at the
    calculated middle index.

    The input list 'arr' is not modified.

    Args:
        arr: The list of elements.
        left: The left index of the range.
        right: The right index of the range.

    Returns:
        The index of the middle element between 'left' and 'right'.

    '''

    global count

    mid = (left + right) // 2
    count += 1
    
    if arr[left] <= arr[mid] <= arr[right] or arr[right] <= arr[mid] <= arr[left]:
        return mid
    elif arr[mid] <= arr[left] <= arr[right] or arr[right] <= arr[left] <= arr[mid]:
        return left
    else:
        return right


def quick_sort(data):

    '''
    This function implements the quicksort algorithm to sort a given
    list of data in ascending order. It recursively divides the list
    into smaller sublists, selects a pivot element, partitions the
    list based on the pivot, and then sorts the sublists individually.

    The input list 'data' is not modified. The function creates new
    lists during the sorting process.

    Args:
        data: The list of elements to be sorted.

    Returns:
        A new list containing the sorted elements of the input list.
    
    '''

    global count

    if len(data) > 1:
        pivot_ind = getmid_index(data,0,len(data)-1)
        pivot = data[pivot_ind]
        data[pivot_ind], data[len(data)-1] = data[len(data)-1], data[pivot_ind]

        i = 0
        j = len(data) - 2
        count += 1
        i = partition(data,i,j,pivot)
        return quick_sort(data[:i]) + [pivot] + quick_sort(data[i+1:])
    else:
        return data


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

    quick_sort(random_lst)

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

    quick_sort(random_lst)

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

    quick_sort(random_lst)

    print("Average case scenario is:", count)


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    count = 0

    random_lst = random_list(20)
    print(f"Random list is : {random_lst}")

    sorted_val = quick_sort(random_lst)
    print(f"Sorted list is: {sorted_val}")
    print(f"Count is : {count}")

    k = 10

    while k <= 10000:
        count = 0
        start = time.time()
        quick_sort(random_list(k))
        end = time.time()
        print(f"k is {k} and count is : {count}")
        print(f"Time taken is: {end - start}")
        print()
        k *= 10
    
    k = 20000
    count = 0
    start = time.time()
    quick_sort(random_list(k))
    end = time.time()
    print(f"k is {k} and count is : {count}")
    print(f"Time taken is: {end - start}")
    print()

    k = 50000
    count = 0
    start = time.time()
    quick_sort(random_list(k))
    end = time.time()
    print(f"k is {k} and count is : {count}")
    print(f"Time taken is: {end - start}")
    print()

    print("For size 1000:\n")
    count = 0

    avg_scenario(1000)

    count = 0

    best_scenario(1000)

    count = 0

    worst_scenario(1000)
