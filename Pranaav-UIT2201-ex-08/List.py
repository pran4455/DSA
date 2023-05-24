# -*- coding: utf-8 -*-

import ctypes
from timeit import default_timer

class List:

    def __init__(self,val):

        '''
        A List is a dynamic array implementation in Python that allows
        for efficient appending, indexing, and iteration of elements.
        Initializes a new instance of the List class.

        Parameters:
        val: An integer value specifying the initial capacity of the list.
        
        '''
        
        if isinstance(val, int):
            self.n = 0
            self.capacity = val
            self.lst = self.makearray(val)

    

    def __len__(self):

        '''
        Returns the number of elements in the list.
    
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
        Appends the specified element to the end of the list.

        Parameters:
        element: The element to append to the end of the list.

        '''

        if self.n == self.capacity:
            self.lst = self.resize(2 * self.capacity)

        self.lst[self.n] = element
        self.n += 1

    def resize(self, cap):

        '''
        Resizes the list to the specified capacity.

        Parameters:
        cap: The new capacity of the list.

        Returns:
        The new capacity of the list.
    
        '''

        new_arr = self.makearray(cap)
        for i in range(len(self.lst)):
            new_arr[i] = self.lst[i]
        return new_arr
    
    def __getitem__(self,ind):

        '''
        Gets the element at the specified index from the list.

        Parameters:
        ind: The index of the element to get.

        Returns:
        The element at the specified index from the list.
    
        '''

        return self.lst[ind]
    
    def __setitem__(self,ind,ele):

        '''
        Sets the element at the specified index in the list to the
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
        Converts the list to a string.

        Returns:
        A string representation of the list.
    
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
        a = List(size)

        start = default_timer()
        for i in range(size+1):
            a.append(i)
        end = default_timer()

        print(f"SIZE : {size} \nTIME : {(end - start)} \nRATIO : {(end - start)/size} \n")
