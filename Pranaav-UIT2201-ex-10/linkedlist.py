# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the singly linked
list created using a Node class. This is a part of the 
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
        Node class represents a node in a singly linked list.

        Args:
            item: The item/value stored in the node.
            next: Reference to the next node.

        '''

        self.item = item
        self.next = next


class SinglyLinkedList:


    '''
    The SinglyLinkedList class represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
        tail (Node): The tail node of the linked list.

    Methods:
        __init__(): Initializes an empty linked list with a head and tail node.
        isempty(): Checks if the linked list is empty.
        append(ele): Appends an element to the end of the linked list.
        __str__(): Returns a string representation of the linked list.
        find(ele): Searches for an element in the linked list and returns itsposition.
        __contains__(ele): Checks if an element is present in the linked list.
        findprev(ind): Finds the previous node at a given index in the linked list.
        pop(ind): Removes and returns the element at the given index in the linked list.

    '''


    def __init__(self):

        '''
        Initializes an empty linked list with a head and tail node.

        '''
        
        self.head = self.tail = Node()


    def isempty(self):

        '''
        Checks if the linked list is empty.

        Returns:
            True if the linked list is empty, False otherwise.

        '''

        return self.head == self.tail


    def append(self, ele):

        '''
        Appends an element to the end of the linked list.

        Args:
            ele: The element to be appended.

        '''

        temp = Node(ele)
        self.tail.next = temp
        self.tail = temp


    def __str__(self):

        '''
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list.

        '''

        pos = self.head.next
        s = '['

        while pos is not None:
            s += str(pos.item) + ','
            pos = pos.next

        if s[-1] == ',':
            s = s[:-1]

        return s + ']'


    def find(self, ele):

        '''
        Searches for an element in the linked list and returns its position.

        Args:
            ele: The element to search for.

        Returns:
            The position/index of the element if found, -1 otherwise.

        '''

        pos = self.head.next
        ct = 0

        while pos is not None:
            if pos.item == ele:
                return ct

            ct += 1
            pos = pos.next

        return -1


    def __contains__(self, ele):

        '''
        Checks if an element is present in the linked list.

        Args:
            ele: The element to check for.

        Returns:
            True if the element is present, False otherwise.

        '''

        pos = self.head.next

        while pos is not None:
            if pos.item == ele:
                return True

            pos = pos.next

        return False


    def findprev(self, ind):

        '''
        Finds the previous node at a given index in the linked list.

        Args:
            ind: The index for which to find the previous node.

        Returns:
            The previous node at the given index.

        '''

        if ind > 0:
            pos = self.head.next

            for i in range(ind - 1):
                pos = pos.next

            return pos

        else:
            return self.head


    def pop(self, ind):

        '''
        Removes and returns the element at the given index in the linked list.

        Args:
            ind: The index of the element to be removed.

        Returns:
            The element removed from the linked list.

        Raises:
            Exception: If the linked list is empty.
            
        '''

        if self.isempty():
            raise Exception("Empty list")
        else:
            pos = self.findprev(ind)
            pop_item = pos.next.item
            pos.next = pos.next.next

        return pop_item


    def insert(self, ind, ele):

        '''
        Inserts an element at the given index in the linked list.

        Args:
            ind: The index at which the element should be inserted.
            ele: The element to be inserted.

        '''

        pos = self.findprev(ind)
        temp = Node(ele)
        temp_pos = pos.next.next
        pos.next = temp
        pos.next.next = temp_pos


    def remove(self, ele):

        '''
        Removes the first occurrence of the given element from the linked list.

        Args:
            ele: The element to be removed.

        Raises:
            Exception: If the element is not found in the list.

        '''

        prev = self.findprev(ele)
        delnode = prev.next

        if delnode is None:
            raise Exception("Element is not in list!")
        prev.next = delnode.next
            
        self.size -= 1


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    a = SinglyLinkedList()

    a.append(5)
    a.append(6)
    a.append(8)
    a.append(10)
    a.append(12)
    a.append(40)
    a.append(50)
    a.append(60)
    a.insert(7,90)

    print("Current linked list is :")
    print(a)
    print()

    print("Now popping randomly.")
    print(a.pop(7))
    print(a)
    print()
    
    print(a.pop(2))
    print(a)
    print()


