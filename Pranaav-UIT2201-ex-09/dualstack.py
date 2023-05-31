# -*- coding: utf-8 -*-


'''
This module provides a class called dualstack that implements a
data structure to maintain two stacks in a single array. This
is a part of the exercises given under the course UIT2201
(Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Wed May 31 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import ctypes


class dualstack:


    '''

    The dualstack class represents a data structure that combines two
    stacks in a single array.

    Attributes:
        top1 (int): The index representing the top element of the first stack.
        top2 (int): The index representing the top element of the second stack.
        array (ctypes array): The array used to store the elements of the stacks.
        n (int): The size of the array.

    Methods:
        makearray(size): Creates a new array of the specified size.
        push(ind, ele): Pushes an element onto the specified stack.
        pop(ind): Pops and returns the top element from the specified stack.
        __setitem__(ind, ele): Sets the element at the specified index in the array.
        __str__(): Returns a string representation of the dualstack.
        isfull(): Checks if the dualstack is full.

    '''


    def __init__(self, size):

        '''

        Initializes a dualstack object with the specified size.

        Args:
            size (int): The size of the dualstack.

        '''


        self.top1 = 0
        self.top2 = size - 1
        self.array = self.makearray(size)
        self.n = size


    def makearray(self, size):
        '''

        Creates a new array of the specified size.

        Args:
            size (int): The size of the new array.

        Returns:
            A new array of the specified size.

        '''

        B = (size * ctypes.py_object)()
        return B


    def push(self, ind, ele):

        '''

        Pushes an element onto the specified stack.

        Args:
            ind (int): The index of the stack to push the element onto.
            ele: The element to be pushed.

        Raises:
            Exception: If the stack is full (overflow).

        '''

        if ind == 0:

            if not self.isfull():
                self.array[self.top1] = ele
                self.top1 += 1
            else:
                raise Exception("Stack overflow")
            
        else:

            if not self.isfull():
                self.array[self.top2] = ele
                self.top2 -= 1
            else:
                raise Exception("Stack overflow")
            

    def pop(self, ind):

        '''

        Pops and returns the top element from the specified stack.

        Args:
            ind (int): The index of the stack to pop the element from.

        Returns:
            The element removed from the top of the stack.

        Raises:
            Exception: If the stack is empty (underflow).

        '''

        if ind == 0:

            try:

                if self.top1 >= 0:
                    pop_ele = self.array[self.top1]
                    self.array[self.top1] = ctypes.py_object()
                    self.top1 -= 1
                    return pop_ele
                else:
                    raise Exception("Stack underflow")
                
            except:

                self.top1 -= 1
                if self.top1 >= 0:
                    pass
                else:
                    raise Exception("Stack underflow")
                return None
            
        else:

            try:

                if self.top2 < self.n:
                    pop_ele = self.array[self.top2]
                    self.array[self.top2] = ctypes.py_object()
                    self.top2 += 1
                    return pop_ele
                else:
                    raise Exception("Stack underflow")
                
            except:

                self.top2 += 1
                if self.top2 < self.n:
                    pass
                else:
                    raise Exception("Stack underflow")
                return None


    def __setitem__(self, ind, ele):

        '''

        Sets the element at the specified index in the array to the specified value.

        Args:
            ind (int): The index of the element to set.
            ele: The new value for the element at the specified index.

        Raises:
            IndexError: If the index is out of range.

        '''

        if ind <= self.n:
            self.n += 1
            self.array[ind] = ele
        else:
            raise IndexError("Index out of range")


    def __str__(self):

        '''

        Returns a string representation of the dualstack.

        Returns:
            A string representation of the dualstack.

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
                out += '-,'
        out = out.rstrip(',')
        return out + '>'


    def isfull(self):

        '''

        Checks if the dualstack is full.

        Returns:
            True if the dualstack is full, False otherwise.

        '''

        if self.top1 > self.top2:

            return True
        
        return False


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    dual_stack = dualstack(10)

    for i in range(1,6):

        dual_stack.push(0,i)
        print(dual_stack)

    print(dual_stack)
    print()

    for j in range(100,105):

        dual_stack.push(1,j)
        print(dual_stack)

    print(dual_stack)
    print()

    #now checking if it is full
    print(f"Is the stack full : {dual_stack.isfull()}")
    print()

    for i in range(5):

        dual_stack.pop(0)
        print(dual_stack)

    print(dual_stack)
    print()

    for j in range(5):

        dual_stack.pop(1)
        print(dual_stack)

    print(dual_stack)
    print()

    #now removing everything
    dual_stack.pop(0)
    dual_stack.pop(1)

    print(dual_stack)
    print()
