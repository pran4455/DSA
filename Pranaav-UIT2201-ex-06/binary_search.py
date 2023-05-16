# -*- coding: utf-8 -*-

import random
from time import time 


def binary_search(data,s_ele,high,low=0):

    '''
    The binary_search function performs a binary search on a sorted
    list of data to find a specified element.

    Args:
        data (list): A sorted list of elements to search in.
        s_ele (int or float): The element to search for in the data.
        high (int): The index of the highest element in the data.
        low (int, optional): The index of the lowest element in the
        data. Default is 0.

    Assumptions:
        The input data list is sorted in ascending order.
        The input high value is valid and within the bounds
        of the data list.
        The input low value is valid and within the bounds
        of the data list.

    Returns:
        If the element s_ele is found in the data, the
        function returns its index.
        If the element s_ele is not found in the data, the
        function returns -1.

    '''

    if low <= high:

        mid = (low + high) // 2        

        if data[mid] == s_ele:
            return mid
        
        elif data[mid] < s_ele:
            return binary_search(data,s_ele,high,mid+1)
        
        elif data[mid] > s_ele:
            return binary_search(data,s_ele,mid-1,low)
        
    else:

        return -1
        

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


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module


    random_lst = [x for x in range(1,10000001)]

    search_val = random_lst[0]
    start = time()
    ind = binary_search(random_lst,search_val,len(random_lst)-1)
    end = time()

    print(f"Actual index : 0 , index found via binary search : {ind}")
    print("Time taken is :", end - start)

    random_lst = [x for x in range(1,10000001)]

    search_val = random_lst[-1]
    start = time()
    ind = binary_search(random_lst,search_val,len(random_lst)-1)
    end = time()

    print(f"Actual index : 0 , index found via binary search : {ind}")
    print("Time taken is :", end - start)

    random_lst = [x for x in range(1,10000001)]

    search_val = 100000000
    start = time()
    ind = binary_search(random_lst,search_val,len(random_lst)-1)
    end = time()

    print(f"Element is not present in list, index found via binary search : {ind}")
    print("Time taken is :", end - start)