# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the circular queue
data structure in python using array implementation. This is a part of the 
exercises given under the course UIT2201 (Programming and Data
Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Wed June 7 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import sys
sys.path.append('D:\college files\DSA')
from QueueWrapper import QueueWrapper
import ctypes


class CircularQueue:

    '''
    The CircularQueue class is a wrapper class that provides a simple implementation
    of a circular queue data structure.

    Attributes:
        queue (list): A list representing the queue elements.
        rear (int): The index representing the rear element of the queue.
        front (int): The index representing the front element of the queue.
        cap (int): The maximum capacity of the queue.

    Methods:
        enqueue(ele): Adds an element to the end of the queue.
        dequeue(): Removes and returns the element from the front of the queue.
        is_full(): Checks if the queue is full.
        is_empty(): Checks if the queue is empty.
        rear_element(): Returns the rear element of the queue without removing it.
        peek(): Returns the element from the front of the queue without removing it.
        __contains__(ele): Checks if the given element is present in the queue.
        __getitem__(ind): Gets the element at the specified index from the queue.
        __setitem__(ind, ele): Sets the element at the specified index in the queue to the specified value.
        __str__(): Returns a string representation of the queue.
        __len__(): Returns the number of elements in the queue.

    '''

    def __init__(self, cap):

        '''
        Initializes an empty CircularQueue object.

        Parameters:
            cap (int): The maximum capacity of the queue.

        '''

        self.queue = self.make_queue(cap)
        self.rear = self.front = 0
        self.cap = cap


    def make_queue(self, size):

        '''
        Creates a new queue of the specified size.

        Parameters:
            size (int): The size of the new queue.

        Returns:
            A new queue of the specified size.

        '''

        B = (size * ctypes.py_object)()
        return B


    def enqueue(self, ele):

        '''
        Adds an element to the end of the queue.

        Parameters:
            ele: The element to be added to the queue.

        '''

        if self.is_full():
            raise Exception("Queue is full")
        else:
            self.queue[self.rear] = ele
            self.rear = self.next(self.rear)


    def is_full(self):

        '''
        Checks if the queue is full.

        Returns:
            True if the queue is full, False otherwise.

        '''

        return (self.rear + 1) % self.cap == self.front


    def next(self, val):

        '''
        Returns the next index in the circular queue.

        Parameters:
            val (int): The current index.

        Returns:
            The next index in the circular queue.

        '''

        val = (val + 1) % self.cap
        return val


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
            pop_ele = self.queue[self.front]
            self.queue[self.front] = ctypes.py_object()
            self.front = self.next(self.front)
            return pop_ele
        

    def is_empty(self):

        '''
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.

        '''

        return self.rear == self.front


    def rear_element(self):

        '''
        Returns the rear element of the queue without removing it.

        Returns:
            The rear element of the queue.

        '''

        return self.queue[self.rear - 1]


    def peek(self):

        '''
        Returns the element from the front of the queue without
        removing it.

        Returns:
            The element from the front of the queue.

        '''

        return self.queue[self.front]


    def __contains__(self, ele):

        '''
        Check if the given element is present in the queue.

        Parameters:
            ele: The element to check for presence in the queue.

        Returns:
            bool: True if the element is found in the queue, False
            otherwise.

        '''

        try:
            for i in self.queue:
                if ele == i:
                    return True
        except:
            return False
        return False


    def __getitem__(self, ind):

        '''
        Gets the element at the specified index from the queue.

        Parameters:
            ind (int): The index of the element to get.

        Returns:
            The element at the specified index from the queue.

        '''

        return self.queue[ind]


    def __setitem__(self, ind, ele):

        '''
        Sets the element at the specified index in the queue to the specified value.

        Parameters:
            ind (int): The index of the element to set.
            ele: The new value for the element at the specified index.

        '''

        if ind <= self.n:
            self.n += 1
            self.queue[ind] = ele
        else:
            raise IndexError("Index out of range")


    def __str__(self):

        '''
        Converts the queue to a string.

        Returns:
            A string representation of the queue.

        '''

        out = '<'

        for i in range(self.front, self.cap):
            try:
                if i != (self.cap - 1):
                    out += str(self.queue[i])
                    out += ','
                else:
                    out += str(self.queue[i])
            except:
                continue
        return out + '>'
    

    def __len__(self):

        '''
        Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.

        '''

        return len(self.queue)


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    Order_circular_queue = CircularQueue(7)

    print("Checking whether queue is empty : ", Order_circular_queue.is_empty())
    print()

    print("Now adding orders to queue while taking M to be 6")
    print()

    # Add orders to the queue
    Order_circular_queue.enqueue("Pizza")
    Order_circular_queue.enqueue("Burger")
    Order_circular_queue.enqueue("Dosa")
    Order_circular_queue.enqueue("Idly")
    Order_circular_queue.enqueue("Pasta")
    Order_circular_queue.enqueue("Lasagne") # Queue is full, cannot accept more orders

    print("Checking whether queue is full : ", Order_circular_queue.is_full())
    print()

    # Serve orders from the queue
    print("Dequeueing orders : ")
    print()

    print(Order_circular_queue.dequeue())  # Pizza served
    print(Order_circular_queue.dequeue())  # Burger served
    print(Order_circular_queue.dequeue())  # Dosa served
    print(Order_circular_queue.dequeue())  # Idly served
    print(Order_circular_queue.dequeue())  # Pasta served
    print(Order_circular_queue.dequeue())  # Lasagne served