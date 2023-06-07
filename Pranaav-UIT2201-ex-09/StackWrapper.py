# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the stack data 
structure in python using wrapper method. This is a part of the 
exercises given under the course UIT2201 (Programming and Data
Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Wed May 31 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


class StackWrapper:

    '''

    The StackWrapper class is a wrapper class that provides a simple
    implementation of a stack data structure.

    Attributes:
        stack (list): A list representing the stack elements.
        top (int): The index representing the top element of the stack.

    Methods:
        push(ele): Adds an element to the top of the stack.
        pop(): Removes and returns the element from the top of the stack.
        is_empty(): Checks if the stack is empty.
        top_ele(): Returns the top element of the stack without removing it.
        __str__(): Returns a string representation of the stack.
        __len__(): Returns the number of elements in the stack.

    '''


    def __init__(self):

        '''
        Initializes an empty StackWrapper object.

        '''

        self.stack = []
        self.top = 0


    def push(self, ele):

        '''

        Adds an element to the top of the stack.

        Args:
            ele: The element to be added to the stack.

        '''

        self.stack.append(ele)
        self.top += 1


    def pop(self):

        '''

        Removes and returns the element from the top of the stack.

        Returns:
            The element removed from the top of the stack.

        Raises:
            Exception: If the stack is empty (underflow).

        '''

        if self.is_empty():
            raise Exception("Stack Underflow")
        else:
            pop_ele = self.stack.pop()
            self.top -= 1
            return pop_ele
        

    def is_empty(self):

        '''

        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.

        '''

        return len(self.stack) == 0
    

    def top_ele(self):

        '''

        Returns the top element of the stack without removing it.

        Returns:
            The top element of the stack.

        '''

        return self.stack[self.top - 1]
    

    def __str__(self):

        '''

        Returns a string representation of the stack.

        Returns:
            A string representation of the stack.

        '''

        return str(self.stack)
    

    def __len__(self):
        
        '''

        Returns the number of elements in the stack.

        Returns:
            The number of elements in the stack.

        '''

        return len(self.stack)
