# -*- coding: utf-8 -*-


'''
This module provides a class for implementation of the doubly linked
list created using a DNode that inherits the Node. This is a part of the 
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
            item: The item/value stored in the Dnode.
            next: Reference to the next Dnode.

        '''

        self.item = item
        self.next = next


class DNode(Node):

    __slots__ = ['item', 'next', 'prev']

    def __init__(self,item=None,next=None,prev=None):

        '''
        DNode class represents a Dnode in a singly linked list.

        Args:
            item: The item/value stored in the node.
            next: Reference to the next node.
            prev: Reference to the previous node.

        '''

        super().__init__(item,next)
        self.prev = prev


class doublylinkedlist:


    '''
    This class represents a doubly linked list data structure.

    Attributes:
        head: A reference to the head (first) Dnode in the linked list.
        tail: A reference to the tail (last) Dnode in the linked list.
        size: The number of elements in the linked list.

    Methods:
        __init__(): Initializes an empty doubly linked list.
        append(ele): Adds an element to the end of the linked list.
        insert(ind, ele): Inserts an element at the specified index in the
        linked list.
        findprev(ind): Returns the Dnode before the specified index in the
        linked list.
        __str__(): Returns a string representation of the linked list.
        reverse_display(): Returns a string representation of the linked list
        in reverse order.
        pop(ind=None): Removes and returns the element at the specified index
        in the linked list.
        __len__(): Returns the number of elements in the linked list.

    '''

    def __init__(self):

        '''
        Initializes an empty doubly linked list.

        The head and tail Dnodes are created, and the size is set to 0.

        '''

        self.head = self.tail = DNode()
        self.size = 0


    def append(self, ele):

        '''
        Adds an element to the end of the linked list.

        Args:
            ele: The element to be added to the linked list.

        '''

        temp = DNode(ele)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1


    def insert(self, ind, ele):
        
        '''
        Inserts an element at the specified index in the linked list.

        Args:
            ind: The index at which to insert the element.
            ele: The element to be inserted.

        Raises:
            Exception: If the index is invalid.

        '''

        if ind > 0 and ind < self.size - 2:

            pos = self.findprev(ind)
            temp = DNode(ele)
            pos.next.prev = temp
            temp.next = pos.next
            pos.next = temp
            temp.prev = pos
            self.size += 1

        elif ind == self.size - 1:
            self.append(ele)
        else:
            raise Exception("Invalid index")


    def findprev(self, ind):

        '''
        Returns the Dnode before the specified index in the linked list.

        Args:
            ind: The index of the Dnode to find.

        Returns:
            The Dnode before the specified index.

        Raises:
            Exception: If the index is invalid.

        '''

        if ind < self.size:
            if ind > 0:
                pos = self.head.next
                for i in range(ind - 1):
                    pos = pos.next
                return pos
            else:
                return self.head
        else:
            raise Exception("Invalid index")


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


    def reverse_display(self):

        '''
        Returns a string representation of the linked list in reverse order.

        Returns:
            A string representation of the linked list in reverse order.

        '''

        pos = self.tail
        s = '['
        while pos is not None and pos.item is not None:
            s += str(pos.item) + ','
            pos = pos.prev
        if s[-1] == ',':
            s = s[:-1]
        return s + ']'


    def pop(self, ind=None):

        '''
        Removes and returns the element at the specified index in the linked list.

        If no index is provided, the element at the end of the linked list is
        removed.

        Args:
            ind: The index of the element to remove. Default is None.

        Returns:
            The removed element.

        Raises:
            Exception: If the index is invalid.

        '''

        if ind is None:
            pos = self.tail.prev
            pop_val = pos.next.item
            self.tail.prev = None
            pos.next = None
            self.tail = pos
            self.size -= 1
            return pop_val
        
        else:
            pos = self.findprev(ind)
            pop_val = pos.next.item
            pos.next.next.prev = pos
            pos.next = pos.next.next
            self.size -= 1
            return pop_val


    def __len__(self):

        '''
        Returns the number of elements in the linked list.

        Returns:
            The number of elements in the linked list.

        '''

        return self.size


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    a = doublylinkedlist()

    a.append(10)
    a.append(20)
    a.append(30)
    a.append(40)
    a.append(50)
    a.append(60)
    a.insert(1,10000)

    print(f"Current list is : {a}")
    print()

    a.insert(1,20000)
    print(f"Current list is : {a}")
    print()

    a.insert(1,30000)
    print(f"Current list is : {a}")
    print()

    a.insert(1,40000)
    print(f"Current list is : {a}")
    print()

    print(f"Pop element is : {a.pop()}")
    print(f"Current list is : {a}")
    print()

    print(f"Pop element is : {a.pop(2)}")
    print(f"Current list is : {a}")
    print()

    print(f"Pop element is : {a.pop(4)}")
    print(f"Current list is : {a}")
    print()

    print("Now printing the reverse display")
    print(a.reverse_display())