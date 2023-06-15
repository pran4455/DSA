# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the linked array
created using a Node that inherits the Node. This is a part of the 
exercises given under the course UIT2201 (Programming and Data
Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed June 10 2023

Revised on Wed June 12 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


class Node:

    __slots__ = ['item', 'next']

    def __init__(self,item=None,next=None):

        '''
        Node class represents a node in a singly linked list.

        Args:
            item: The item/value stored in the Dnode.
            next: Reference to the next Dnode.

        '''

        self.item = item
        self.next = next


class LinkedArray:


    '''
    This is the implementation of a linked array using linked lists.

    Methods:

        init(): Initializes an empty LinkedArray object.
        push(ele): Pushes an element onto the top of the stack.
        pop(): Removes and returns the element from the top of the stack.
        peek(): Returns the element from the top of the stack without removing it.
        isempty(): Checks if the stack is empty.
        str(): Returns a string representation of the stack.
    
    '''


    def __init__(self):

        '''
        Initializes an empty LinkedArray object.

        '''

        self.top = Node()
        self.size = 0


    def push(self, ele):

        '''
        Pushes an element onto the top of the stack.

        Args:
            ele: The element to be pushed onto the stack.

        '''

        temp = Node(ele)
        pos = self.top.next
        self.top.next = temp
        temp.next = pos
        self.size += 1


    def pop(self):

        '''
        Removes and returns the element from the top of the stack.

        Returns:
            The element removed from the top of the stack.

        Raises:
            Exception: If the stack is empty (stack underflow).
            
        '''

        if self.isempty():
            raise Exception("Stack underflow")
        else:
            del_val = self.top.next.item
            self.top.next = self.top.next.next
            self.size -= 1
            return del_val


    def peek(self):

        '''
        Returns the element from the top of the stack without removing it.

        Returns:
            The element from the top of the stack.

        Raises:
            Exception: If the stack is empty.
            
        '''

        if self.isempty():
            raise Exception("Stack is empty")
        else:
            return self.top.next.item


    def isempty(self):

        '''
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.

        '''

        return self.top.next is None


    def __str__(self):

        '''
        Returns a string representation of the stack.

        Returns:
            A string representation of the stack.

        '''

        pos = self.top.next
        s = ''
        while pos is not None:
            d = str(pos.item)
            s += d[::-1] + ','
            pos = pos.next

        if s[-1] == ',':
            s = s[:-1]

        return '[' + s[::-1] + ']'


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    a = LinkedArray()

    a.push(10)
    a.push(20)
    a.push(30)
    a.push(40)
    a.push(50)
    a.push(60)

    print(f"Current array is : {a}")

    print(f"Pop element is : {a.pop()}")
    print(a)
    print()

    print(f"Pop element is : {a.pop()}")
    print(a)
    print()

    print(f"Pop element is : {a.pop()}")
    print(a)
    print()

    print(f"Final element is : {a.peek()}")
    print()

    print(f"Checking if stack is empty : {a.isempty()}")
    print()