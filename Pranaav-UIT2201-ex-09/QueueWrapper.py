# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the queue data 
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


class QueueWrapper:

    '''
    The QueueWrapper class is a wrapper class that provides a simple implementation
    of a queue data structure.

    Attributes:
        queue (list): A list representing the queue elements.
        top (int): The index representing the top element of the queue.

    Methods:
        enqueue(ele): Adds an element to the end of the queue.
        dequeue(): Removes and returns the element from the front of the queue.
        is_empty(): Checks if the queue is empty.
        top_ele(): Returns the top element of the queue without removing it.
        peek(): Returns the element from the front of the queue without removing it.
        __str__(): Returns a string representation of the queue.
        __len__(): Returns the number of elements in the queue.

    '''

    def __init__(self):

        '''
        Initializes an empty QueueWrapper object.

        '''
        
        self.queue = []
        self.top = 0


    def enqueue(self, ele):

        '''
        Adds an element to the end of the queue.

        Args:
            ele: The element to be added to the queue.


        '''
        self.queue.append(ele)
        self.top += 1


    def dequeue(self):

        '''
        Removes and returns the element from the front of the queue.

        Returns:
            The element removed from the front of the queue.

        Raises:
            Exception: If the queue is empty.

        '''

        if self.is_empty():
            raise Exception("Empty Queue")
        else:
            pop_ele = self.queue.pop(0)
            self.top -= 1
            return pop_ele
        

    def is_empty(self):

        '''
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.

        '''

        return len(self.queue) == 0
    

    def top_ele(self):
        
        '''
        Returns the top element of the queue without removing it.

        Returns:
            The top element of the queue.

        '''

        return self.queue[self.top - 1]
    

    def peek(self):

        '''
        Returns the element from the front of the queue without removing it.

        Returns:
            The element from the front of the queue.

        '''

        return self.queue[0]
    

    def __str__(self):

        '''
        Returns a string representation of the queue.

        Returns:
            A string representation of the queue.

        '''

        return str(self.queue)
    

    def __len__(self):

        '''
        Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.

        '''
        
        return len(self.queue)