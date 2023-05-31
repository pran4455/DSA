# -*- coding: utf-8 -*-


'''
This module provides a class called PQueue that implements a
data structure to maintain two queues in a single data structure
that has one high priority queue and another low priority queue.
This is a part of the exercises given under the course UIT2201
(Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Wed May 31 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import sys
sys.path.append('D:\college files\DSA')
from QueueWrapper import QueueWrapper


class PQueue:

    '''
    The PQueue class represents a priority queue implemented using two
    separate queues: one for high priority elements and another for low
    priority elements.

    Attributes:
        highprio (QueueWrapper): A QueueWrapper instance representing 
        the queue for high priority elements.
        lowprio (QueueWrapper): A QueueWrapper instance representing 
        the queue for low priority elements.
        top1 (int): The index representing the top element of the high 
        priority queue.
        bottom1 (int): The index representing the bottom element of the 
        high priority queue.
        top2 (int): The index representing the top element of the low 
        priority queue.
        bottom2 (int): The index representing the bottom element of the 
        low priority queue.

    Methods:
        enqueue(val, ele): Adds an element to the end of the queue based on 
        its priority level.
        dequeue(): Removes and returns the element from the front of the queue.
        is_empty(val): Checks if the queue is empty based on its priority level.
        peek(val): Returns the element from the front of the queue without 
        removing it based on its priority level.
        __str__(): Returns a string representation of the queue.

    '''

    def __init__(self):

        '''
        Initializes a Priority Queue.

        Creates two QueueWrapper instances, one for high priority elements
        and another for low priority elements. Initializes the top and bottom
        indices for both queues.

        '''    

        self.highprio = QueueWrapper()
        self.lowprio = QueueWrapper()
        self.top1 = 0
        self.bottom1 = 0
        self.top2 = 0
        self.bottom2 = 0
    

    def enqueue(self, val, ele):

        '''
        Adds an element to the end of the queue.

        Args:
            ele: The element to be added to the queue.

        '''
        
        if val == 0:

            self.highprio.enqueue(ele)
            self.top1 += 1

        else:

            self.lowprio.enqueue(ele)
            self.top2 += 1


    def dequeue(self):

        '''
        Removes and returns the element from the front of the queue.

        Returns:
            The element removed from the front of the queue.

        Raises:
            Exception: If the queue is empty.

        '''

        if self.is_empty(0):
            if self.is_empty(1):
                raise Exception("Empty Queue")
            else:
                pop_ele = self.lowprio.dequeue()
                self.bottom2 += 1
                return pop_ele
        else:
            pop_ele = self.highprio.dequeue()
            self.bottom1 -= 1
            return pop_ele
        

    def is_empty(self,val):

        '''
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.

        '''

        if val == 0:

            return len(self.highprio) == 0
        
        else:

            return len(self.lowprio) == 0
        

    def peek(self,val):

        '''
        Returns the element from the front of the queue without removing it.

        Returns:
            The element from the front of the queue.

        '''

        if val == 0:

            return self.highprio[0]
        
        else:

            return self.lowprio[0]
        

    def __str__(self):

        '''
        Returns a string representation of the queue.

        Returns:
            A string representation of the queue.

        '''

        a = str(self.highprio)
        b = str(self.lowprio)

        return "High priority is:" + a + "\nLow priority is:" + b
        

#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    priority_queue = PQueue()

    for i in range(1,6):

        priority_queue.enqueue(0,i)

    print(priority_queue)
    print()

    for j in range(100,105):

        priority_queue.enqueue(1,j)

    print(priority_queue)
    print()
    print("Now dequeueing high priority elements:")
    print()

    for i in range(5):

        priority_queue.dequeue()
        print(priority_queue)

    print(priority_queue)
    print()
    print("Now dequeueing the remaining elements:")
    print()

    for i in range(5):

        priority_queue.dequeue()
        print(priority_queue)

