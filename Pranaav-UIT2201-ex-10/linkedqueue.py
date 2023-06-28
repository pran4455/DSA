# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the singly linked
queue created using a Node class. This is a part of the 
exercises given under the course UIT2201 (Programming and Data
Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed June 7 2023

Revised on Wed June 10 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


class Node:

    __slots__ = ['item', 'next']

    def __init__(self,item=None,next=None):

        '''
        Node class represents a node in a singly linked queue.

        Args:
            item: The item/value stored in the node.
            next: Reference to the next node.

        '''

        self.item = item
        self.next = next


class SinglyLinkedQueue:


    '''
    The SinglyLinkedQueue class represents a singly linked queue.

    Attributes:
        front (Node): The front node of the linked queue.
        rear (Node): The rear node of the linked queue.

    Methods:
        __init__(): Initializes an empty linked queue with a front and rear node.
        isempty(): Checks if the linked queue is empty.
        enqueue(ele): enqueues an element to the end of the linked queue.
        __str__(): Returns a string representation of the linked queue.
        find(ele): Searches for an element in the linked queue and returns itsposition.
        __contains__(ele): Checks if an element is present in the linked queue.
        findprev(ind): Finds the previous node at a given index in the linked queue.
        dequeue(): Removes element at the front of linked queue.

    '''


    def __init__(self):

        '''
        Initializes an empty linked queue with a front and rear node.

        '''
        
        self.front = self.rear = Node()


    def isempty(self):

        '''
        Checks if the linked queue is empty.

        Returns:
            True if the linked queue is empty, False otherwise.

        '''

        return self.front.item == None


    def enqueue(self, ele):

        '''
        enqueues an element to the end of the linked queue.

        Args:
            ele: The element to be enqueued.

        '''

        if not(self.isempty()):
            temp = Node(ele)
            self.rear.next = temp
            self.rear = temp
        
        else:
            self.rear.item = ele


    def __str__(self):

        '''
        Returns a string representation of the linked queue.

        Returns:
            A string representation of the linked queue.

        '''

        pos = self.front
        s = '['

        while pos is not None:
            s += str(pos.item) + ','
            pos = pos.next

        if s[-1] == ',':
            s = s[:-1]

        return s + ']'


    def find(self, ele):

        '''
        Searches for an element in the linked queue and returns its position.

        Args:
            ele: The element to search for.

        Returns:
            The position/index of the element if found, -1 otherwise.

        '''

        pos = self.front.next
        ct = 0

        while pos is not None:
            if pos.item == ele:
                return ct

            ct += 1
            pos = pos.next

        return -1


    def __contains__(self, ele):

        '''
        Checks if an element is present in the linked queue.

        Args:
            ele: The element to check for.

        Returns:
            True if the element is present, False otherwise.

        '''

        pos = self.front.next

        while pos is not None:
            if pos.item == ele:
                return True

            pos = pos.next

        return False


    def findprev(self, ind):

        '''
        Finds the previous node at a given index in the linked queue.

        Args:
            ind: The index for which to find the previous node.

        Returns:
            The previous node at the given index.

        '''

        if ind > 0:
            pos = self.front.next

            for i in range(ind - 1):
                pos = pos.next

            return pos

        else:
            return self.front


    def dequeue(self):

        '''
        Removes and returns the element at the given index in the linked queue.

        Args:
            ind: The index of the element to be removed.

        Returns:
            The element removed from the linked queue.

        Raises:
            Exception: If the linked queue is empty.
            
        '''

        if self.isempty():
            raise Exception("Empty queue")
        else:
            dequeue_item = self.front.item
            self.front = self.front.next

        return dequeue_item


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    a = SinglyLinkedQueue()

    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(8)
    a.enqueue(10)
    a.enqueue(12)
    a.enqueue(40)
    a.enqueue(50)
    a.enqueue(60)

    print("Current linked queue is :")
    print(a)
    print()

    print("Now dequeueing.")
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()
    
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()

    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()
    
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()
    
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()
    
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()
    
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()
    
    print(f"Dequeue element is : {a.dequeue()}")
    print(f"Queue is : {a}")
    print()