# -*- coding: utf-8 -*-


'''
This module provides two classes that implement stacks and
queues in python and use the two data structures to find whether
a given number is a palindrome or not. This is a part of the 
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


def digits(data):

    digits_list = []

    while data:

        digits_list.append(data%10)
        data //= 10

    return digits_list


def palindrome(n):

    digits_list = digits(n)

    stack = StackWrapper()
    queue = QueueWrapper()


    for val in digits_list:

        stack.push(val)
        queue.enqueue(val)

    while len(stack) != 0:

        if stack.pop() != queue.dequeue():
            

            return False
        
    return True


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    for n in range(10,1000):
        
        if palindrome(n):
            print(f"{n} is a palindrome")

        else:
            print(f"{n} is not a palindrome")

