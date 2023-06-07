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
            self.array = self.makearray(val)

        elif isinstance(val, list) or isinstance(val, tuple):
            self.n = len(val)
            self.capacity = len(val)
            self.array = val

        elif isinstance(val, str):
            self.n = len(val)
            self.capacity = len(val)
            self.array = [i for i in val]
            

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
            self.array = self.resize(2 * self.capacity)

        self.array[self.n] = element
        self.n += 1


    def get_capacity(self):

        """
        Returns the current capacity of the dynamic array.

        Returns:
            The current capacity of the array.

       """
    
        return self.capacity


    def resize(self, cap):

        '''
        Resizes the Array to the specified capacity.

        Parameters:
        cap: The new capacity of the Array.

        Returns:
        The new capacity of the Array.
    
        '''

        new_arr = self.makearray(cap)
        self.capacity = cap

        for i in range(len(self.array)):
            new_arr[i] = self.array[i]
        return new_arr
    

    def extend(self,other):

        '''
        Extends the Array by appending elements from another iterable.

        Parameters:
        other (iterable): An iterable containing elements to be appended.

        Returns:
        None

        Raises:
        None

        '''

        try:
            for i in other:
                self.append(i)
        except:
            None


    def insert(self,ele,ind):

        '''
        Inserts an element at the specified index in the Array.

        Parameters:
        ele: The element to be inserted.
        ind: The index at which the element should be inserted.

        Returns:
        None

        Raises:
        None

        '''

        if self.n > ind:
            for i in range(self.n,ind,-1):

                self[i] = self[i-1]
            
            self[ind] = ele

    
    def delete(self, idx):

        """
        Deletes an element at a given index in the array.

        Args:
            idx: The index of the element to delete.

        Raises:
            IndexError: If the index is out of range

        """

        if not 0 <= idx < self.n:
            raise IndexError("Index out of range.")
        
        for i in range(idx, self.n - 1):
            self.array[i] = self.array[i + 1]
        self.n -= 1

        if self.n < self.capacity // 4:
            self.resize(self.capacity // 2)


    def index(self, elt):

        """
        Checks if an element is present in the array and returns the
        index of the element

        Args:
            elt: Element whose index is to be found out

        Returns:
            idx (int): If the element is found, index of the element
            is returned, else -1.

        """

        for idx in range(0, self.n):
            if self.array[idx] == elt:
                return idx
        return -1
    

    def count(self, count_elt):

        """
        Returns the number of occurrences of an element in the dynamic
        array

        Args:
            count_elt: Element whose number of occurrences is to be found

        Returns:
            count (idx): The number of occurrences of an element in the
            dynamic array

        """

        count = 0
        for idx in range(0, self.n):
            if self.array[idx] == count_elt:
                count += 1
        return count


    def __contains__(self,ele):

        """
        Check if the given element is present in the array.

        Parameters:
        ele (Any): The element to check for presence in the array.

        Returns:
        bool: True if the element is found in the array, False
        otherwise.

        """

        try:
            for i in self.array:
                if ele == i:
                    return True
        except:
            return False
        return False

    
    def __getitem__(self,ind):

        '''
        Gets the element at the specified index from the Array.

        Parameters:
        ind: The index of the element to get.

        Returns:
        The element at the specified index from the Array.
    
        '''

        return self.array[ind]
    
    
    def __setitem__(self,ind,ele):

        '''
        Sets the element at the specified index in the Array to the
        specified value.

        Parameters:
        ind: The index of the element to set.
        ele: The new value for the element at the specified index.

        '''

        if ind <= self.top:
            self.array[ind] = ele

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
                    out += str(self.array[i])
                    out += ','

                else:
                    out += str(self.array[i])
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

        #amortized analysis
        print(f"SIZE : {size} \nTIME : {(end - start)} \nRATIO : {(end - start)/size} \n")

    lst1 = [x for x in range(1,11)]
    lst2 = [2 * x for x in range(1,11)]

    print(f"List number 1 : {lst1}")
    print(f"List number 2 : {lst2}")

    print(f"Appending an element [5] to list 1: {lst1.append(5)}")

    new = Array(3)
    new[0] = 1
    new[1] = 900

    newone = Array(5)
    newone[0] = 500
    newone[1] = 400
    newone.append(1000)

    newone.extend(new)
    print(newone)

    print(1000 in newone)
    print(9000 in newone)

    print(newone)
    print(newone.count(1000))
    print(newone.index(500))

    newone.delete(0)
    print(newone)

    print(newone.get_capacity())