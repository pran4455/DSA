# -*- coding: utf-8 -*-


'''
This module provides a class used for creating an Array by
importing a module ctypes for creating a dynamic array.
This is a part of the excercises given under the course
UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 24 2023

Revised on Wed May 25 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import ctypes
from timeit import default_timer


class Array:

    '''
    The given class gives the implementation of a dynamic array
    in python.

    The input data is not modified in any way and there are
    no side effects.

    methods:
        __init__: the constructor

        __setitem__: for setting a certain value at an index

        __getitem__: for getting a value at an index

        __len__: for finding the length of array

        __str__: for displaying class objects in human readable
        form and return a string form of array.

        makearray: to create an array of a specified size.

        append: to add an element to the end of the array.

        resize: to increase size of array dynamically.

    '''

    def __init__(self,val):

        '''
        A Array is a dynamic array implementation in Python that allows
        for efficient appending, indexing, and iteration of elements.
        Initializes a new instance of the Array class.

        Parameters:
        val: An integer value specifying the initial capacity of the Array.
        
        '''
        
        if isinstance(val, int):
            self.n = 0
            self.capacity = val
            self.lst = self.makearray(val)

        elif isinstance(val, list):
            self.n = 0
            self.capacity = len(val)
            temp = self.makearray(len(val))


    def __len__(self):

        '''
        Returns the number of elements in the Array.
    
        '''

        return self.n
    

    def makearray(self, size):

        '''
        Creates a new array of the specified size.

        Parameters:
        size: The size of the new array.

        Returns:
        A new array of the specified size.
    
        '''

        B = (size * ctypes.py_object)()
        return B
    
    
    def append(self,element):

        '''
        Appends the specified element to the end of the Array.

        Parameters:
        element: The element to append to the end of the Array.

        '''

        if self.n == self.capacity:
            self.lst = self.resize(2 * self.capacity)

        self.lst[self.n] = element
        self.n += 1


    def resize(self, cap):

        '''
        Resizes the Array to the specified capacity.

        Parameters:
        cap: The new capacity of the Array.

        Returns:
        The new capacity of the Array.
    
        '''

        new_arr = self.makearray(cap)
        for i in range(len(self.lst)):
            new_arr[i] = self.lst[i]
        return new_arr
    
    
    def __getitem__(self,ind):

        '''
        Gets the element at the specified index from the Array.

        Parameters:
        ind: The index of the element to get.

        Returns:
        The element at the specified index from the Array.
    
        '''

        return self.lst[ind]
    
    
    def __setitem__(self,ind,ele):

        '''
        Sets the element at the specified index in the Array to the
        specified value.

        Parameters:
        ind: The index of the element to set.
        ele: The new value for the element at the specified index.

        '''

        if ind <= self.n:
            self.n += 1
            self.lst[ind] = ele
        
        else:
            raise IndexError("Index out of range")


    def __str__(self):

        '''
        Converts the Array to a string.

        Returns:
        A string representation of the Array.
    
        '''

        out = '<'
        for i in range(self.n):
            try:
                if i != (self.n - 1):
                    out += str(self.lst[i])
                    out += ','

                else:
                    out += str(self.lst[i])
            except:
                continue

        return out + '>'


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    #initializing different sizes
    sizes = [1, 5, 10, 100, 500, 1000, 5000, 10000, 50000, 100000]

    #this loop calculates the times for appending until size gets extended
    for size in sizes:
        a = Array(size)

        start = default_timer()
        for i in range(size+1):
            a.append(i)
        end = default_timer()

        print(f"SIZE : {size} \nTIME : {(end - start)} \nRATIO : {(end - start)/size} \n")

    lst1 = [x for x in range(1,11)]
    lst2 = [2 * x for x in range(1,11)]

    print(f"List number 1 : {lst1}")
    print(f"List number 2 : {lst2}")

    print(f"Appending an element [5] to list 1: {lst1.append(5)}")
