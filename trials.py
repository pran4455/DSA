import random
from abc import ABCMeta, abstractmethod,ABC

def ins_sort(data):

    n = len(data)

    for i in range(1,n):

        j = i-1
        tempvar = data[i]

        while j>=0 and tempvar < data[j]:

            data[j+1] = data[j]
            j -= 1

        data[j+1] = tempvar

    return data

def random_list(size):

    '''
    The given function generates a random number of values
    and returns the values in a list.

    args:
        size: the number of point objects to be
        generated

    Returns:
        A list of random integer values.
    
    '''

    random_list = []

    for case in range(size):
        x_val = random.randint(-1000,1000)
        random_list.append(x_val)   

    return random_list

def merge(A,B):

    i = 0
    j = 0
    C = []

    while i < len(A) and j < len(B):

        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i < len(A):
        C.extend(A[i:])
    else:
        C.extend(B[j:])
        
    return C           

# print(merge([1,2,5,7,8,80],[-1,0,10,100]))
a = [123,12,31,21,23,123,1,231231]

import ctypes

class dynarray:

    def __init__(self,val):

        if isinstance(val, int):

            self.array = self.makearray(val)
            self.top = 0
            self.size = val
        
        elif isinstance(val, list) or isinstance(val, tuple):

            self.array = self.makearray(len(val))
            for i in val:
                self.array.append(i)
            
            self.size = len(val)
            self.top = len(val) - 1
        
        else:

            raise Exception("Invalid input")
 
    def makearray(self,size):

        temp_arr = (size * ctypes.py_object)()
        return temp_arr

    def resize(self,size):

        temp = self.makearray(size)
        for i in range(self.size):
            temp[i] = self.array[i]

        self.size = size
        return temp

    def __setitem__(self,ind,ele):

        self.array[ind] = ele
    
    def append(self,ele):

        if self.size > self.top:
            self.array[self.top] = ele
            self.top += 1
        
        else:

            val = self.size * 2
            self.array = self.resize(val)
            self.array[self.top] = ele
            self.top += 1

    def __getitem__(self,ind):

        '''
        Gets the element at the specified index from the Array.

        Parameters:
        ind: The index of the element to get.

        Returns:
        The element at the specified index from the Array.
    
        '''

        return self.array[ind]

    def __str__(self):

        s = '['
        try:
            for val in self.array:

                s += str(val) + ','

            if s[-1] == ',':

                s = s[:-1]
        except:
            
            pass
        
        if s[-1] == ',':

            s = s[:-1]

        return s + ']'
    
    def isempty(self):

        pass

    def pop(self,ind=0):

        if not self.isempty():
            if ind == 0:

                pop_ele = self.array[self.top - 1]
                self.array[self.top] = ctypes.py_object
                self.top -= 1
                return pop_ele
            
            else:

                for j in range(ind,self.top - 1):

                    self.array[j] = self.array[j+1]

                print(self.top)     

def insort(data):

    N = len(data)
    for i in range(1,N):
        j = i - 1
        temp = data[i]
        while j >= 0 and temp < data[j]:

            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp

def selsor(data):

    for i in range(len(data)):

        ind = i

        for j in range(i+1,len(data)):

            if data[ind] > data[j]:

                ind = j

        if i != ind:

            data[ind], data[i] = data[i], data[ind]

def mers(a,b):

    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if j < len(b):

        c.extend(b[j:])

    else:

        c.extend(a[i:])

    return c

def mersor(data):

    if len(data) < 2:

        return data[:]
    
    else:
        mid = len(data)//2
        return mers(mersor(data[:mid]),mersor(data[mid:]))

def part(data,i,j,pivot):

    while True:

        while data[i] < pivot:
            
            i += 1
    
        while data[j] > pivot:

            j -= 1

        if i >= j:

            break
    
        data[j], data[i] = data[i], data[j]
        i += 1
        j -= 1

        
    # print(data)
    # print(i)
    data[i] , data[len(data)-1] = data[len(data)-1] , data[i]
    return i

def qs(data):
        
    if len(data) > 2:

        pivot = data[-1]
        i = 0
        j = len(data) - 2
        i = part(data,i,j,pivot)

        return qs(data[:i]) + [pivot] + qs(data[i+1:])
    
    else:

        return data

class List:

    def __init__(self,val):

        if isinstance(val, int):

            self.List = self.makearray(val)
            self.cap = val
            self.size = 0
        
        elif isinstance(val, list,tuple):

            self.List = self.makearray(len(val))
            for i in range(len(val)):

                self.List[i] = val[i]

            self.size = len(val)
            self.cap = len(val)

        else:

            raise Exception("Invalid input")
        
    def makearray(self,size):

        b = (size * ctypes.py_object)()
        self.cap = size
        return b
    
    def resize(self,size):

        temp = self.makearray(size)
        for i in range(self.size):
            temp[i] = self.List[i]

        return temp
    
    def __setitem__(self,ind,val):

        self.List[ind] = val

    def __getitem__(self,ind):

        return self.List[ind]
    
    def isfull(self):

        return self.cap == self.size
    
    def __str__(self):

        s = '['

        
        for i in range(self.size):
                s += str(self.List[i])+','

        if s[-1] == ',':
            s = s[:-1]
        return s + ']'
    
    def append(self,val):
            
        if self.isfull():

            self.List = self.resize(self.cap * 2)
            self.List[self.size] = val
            self.size += 1

        else:

            self.List[self.size] = val
            self.size += 1

    def __len__(self):

        return self.size
    
    def isempty(self):
        if self.size == 0:
            return True
        return False
    
    def pop(self,ind=None):

        if self.isempty():
            raise Exception("Empty list")
        
        else:
            if ind == None:
                pop_ele = self.List[self.size - 1]
                self.List[self.size - 1] = ctypes.py_object()
                self.size -= 1
                return pop_ele
            
            elif ind < self.size:
                
                pop_ele = self.List[ind]
                for i in range(ind,self.size - 1):

                    self.List[i] = self.List[i+1]

                self.List[self.size - 1] = ctypes.py_object()
                self.size -= 1
                return pop_ele
            
            else:
                raise Exception("Invalid index")

    def remove(self,ele):

        ind = 0
        try:
            for val in self.List:
                if val == ele:
                    self.pop(ind)

                ind += 1
        except:
            pass
    
    def insert(self,ind,ele):

        if self.isfull():

            self.List = self.resize(2 * self.cap)

        for i in range(ind,self.size):
            self.List[i+1] = self.List[i]
        self.List[ind] = ele

b = List(5)
x = [i for i in range(10,100,10)]
for i in x:
    b.append(i)

print(b)
b.remove(90)
print(b)
a = list()

class Node:

    __slots__ = ['item','next']

    def __init__(self,item=None,next=None):

        self.item = item
        self.next = next

class LinkedArray:

    def __init__(self):

        self.top = Node()
        self.size = 0

    def push(self,ele):

        temp = Node(ele)
        pos = self.top.next
        self.top.next = temp
        temp.next = pos
        self.size += 1

    def pop(self):

        if self.isempty():
            raise Exception("stack underflow")
        
        else:
            self.top.next = self.top.next.next
            self.size -= 1
    
    def peek(self):

        return self.top.next.item
    
    def isempty(self):

        return self.top.next == None
    
    def __str__(self):

        pos = self.top.next
        s = ''
        while pos is not None:
            d = str(pos.item)
            s += d[::-1] + ','
            pos = pos.next

        if s[-1] == ',':
            s = s[:-1]

        return '[' + s[::-1] + ']'
    
class LinkedQueue:

    def __init__(self):
        pass

class DNode(Node):

    def __init__(self,item=None,next=None,prev=None):

        super().__init__(item,next)
        self.prev = prev
    
class Doublylinked:

    def __init__(self):

        self.head = self.tail = DNode()
        self.size = 0

    def append(self,ele):

        temp = DNode(ele)
        temp.prev = self.tail
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def pop(self):

        self.tail = self.tail.prev
        self.tail.next.prev = None
        self.tail.next = None
        self.size -= 1

    def __str__(self):

        pos = self.head.next
        s = '['
        while pos is not None:
            d = str(pos.item)
            s += d + ','
            pos = pos.next

        if s[-1] == ',':
            s = s[:-1]

        return s + ']'
    
# c = Doublylinked()
# c.append(10)
# c.append(20)
# print(c)

def insertionsort(data):

    for i in range(len(data)):

        temp = data[i]
        j = i - 1
        while j >= 0 and data[j] > temp:

            data[j + 1] = data[j]
            j -= 1
        
        data[j+1] = temp

def selsort(data):

    for i in range(len(data)):

        ind = i

        for j in range(i+1,len(data)):

            if data[j] < data[ind]:

                ind = j

        data[i] , data[ind] = data[ind], data[i]

def bubsort(data):

    for i in range(len(data)):

        for j in range(len(data) - i - 1):

            if data[j] > data[j+1]:

                data[j],data[j+1] = data[j+1],data[j]

def mersor(a,b):

    i = j = 0
    c = []
    while i < len(a) and j < len(b):

        if a[i] < b[j]:

            c.append(a[i])
            i += 1
        
        else:

            c.append(b[j])
            j += 1
    
    if i < len(a):

        c.extend(a[i:])

    else:

        c.extend(b[j:])

    return c

a = [123, 12, 2, 5, 739, 1023123, 10]
b = [1281083, 123112, 1232, 15, 9739, 1023123, 10]
# a.sort()
# b.sort()
# print(mersor(a,b))

def parti(data,i,j,pivot):

    while True:

        while data[i] < pivot:

            i += 1

        while data[j] > pivot:

            j -= 1

        if i >= j:

            break
        
        data[i], data[j] = data[j], data[i]
        i += 1
        j += 1
    
    return i

def qsor(data):

    if len(data) < 2:

        return data
    
    pivot = data[-1]
    i = 0
    j = len(data) - 2
    ind = part(data,i,j,pivot)

    return qsor(data[:ind]) + [pivot] + qsor(data[ind+1:])

# n = qsor(a)
# print(a)
# print(n)

class LinkedCircularQueue:

    def __init__(self):

        self.front = self.rear = Node()
        self.rear.next = self.front
        self.size = 0

    def enqueue(self,ele):

        temp = Node(ele)
        self.rear.next = temp
        self.rear = temp
        temp.next = self.front
        self.size += 1

    def dequeue(self):

        if self.isempty():

            raise Exception("Queue underflow")
    
        else:

            pop_ele = self.front.next.item
            self.front.next = self.front.next.next
            self.size -= 1
            return pop_ele
        
    def isempty(self):

        return self.front.next == self.front

    def __str__(self) -> str:
        
        s = '['

        pos = self.front.next
        while pos is not self.front:

            s += str(pos.item) + ','
            pos = pos.next

        if s[-1] == ',':
            s = s[:-1]

        return s + ']'
    
    
a = LinkedCircularQueue()
a.enqueue(10)
for i in x:

    a.enqueue(i)

print(a)
for i in x:

    # print(a.dequeue())
    # print(a)
    a.dequeue()
print(a)
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
a.enqueue(10)
# print(a)

# list stack queue 

# wrapper linked compact dynamic

class circularqueue:

    def __init__(self,cap):

        self.cap = cap
        self.queue = self.makearray(cap)
        self.front = self.rear = 0
        self.size = 0

    def makearray(self,size):

        b = (size * ctypes.py_object)()
        return b
    
    def __setitem__(self,ind,ele):

        self.queue[ind] = ele

    def next(self,ind):

        return (ind + 1) % self.cap

    def enqueue(self,ele):

        if self.isfull():

            raise Exception("Queue Overflow")
        
        else:

            self.queue[self.rear] = ele
            self.rear = self.next(self.rear)
            self.size += 1
        
    def dequeue(self):

        if self.isempty():

            raise Exception("Queue underflow")
        
        else:

            pop_ele = self.queue[self.front]
            self.queue[self.front] = ctypes.py_object()
            self.front = self.next(self.front)
            self.size -= 1
            return pop_ele
        
    def __getitem__(self,ind):

        return self.queue[ind]

    def isempty(self):

        return self.front == self.rear
    
    def isfull(self):

        return self.next(self.rear) == self.front
    
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
    

    
asman = circularqueue(10)
# for i in x: # x contains some 9 elements
#     asman.enqueue(i)

# print(asman)
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# asman.dequeue()
# print(asman)

def binser(data,ele,low,high):

    if low <= high:

        mid = (low + high) // 2
        if data[mid] == ele:

            return mid
        
        elif data[mid] < ele:

            return binser(data,ele,mid+1,high)

        else:

            return binser(data,ele,low,mid - 1)
    
    else:
        
        return -1
    
x.sort()
a = len(x)
print(x)
print(binser(x,800,0,a-1))

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

    print(a)
    print()

    a.insert(1,20000)
    print(a)
    print()

    a.insert(1,30000)
    print(a)
    print()

    a.insert(1,40000)
    print(a)
    print()

    print(f"Pop element is : {a.pop()}")
    print(a)
    print()

    print(f"Pop element is : {a.pop(2)}")
    print(a)
    print()

    print(f"Pop element is : {a.pop(4)}")
    print(a)
    print()

    print(a.reverse_display())

class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def insert(self, d):
        if self.data == d:
            return False
        elif d < self.data:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def find(self, d):
        if self.data == d:
            return True
        elif d < self.data and self.left:
            return self.left.find(d)
        elif d > self.data and self.right:
            return self.right.find(d)
        return False

    def remove(self, d, parent):
        if d < self.data:
            if self.left:
                return self.left.remove(d, self)
            else:
                return False
        elif d > self.data:
            if self.right:
                return self.right.remove(d, self)
            else:
                return False
        else:
            if self.left is None and self.right is None:
                if parent.left is self:
                    parent.left = None
                else:
                    parent.right = None
                return True
            elif self.left and self.right is None:
                if parent.left is self:
                    parent.left = self.left
                else:
                    parent.right = self.left
                return True
            elif self.right and self.left is None:
                if parent.left is self:
                    parent.left = self.right
                else:
                    parent.right = self.right
                return True
            else:
                moveNodeParent = self
                moveNode = self.right
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.data = moveNode.data
                if moveNode.right:
                    if moveNode.data < moveNodeParent.data:
                        moveNodeParent.left = moveNode.right
                    else:
                        moveNodeParent.right = moveNode.right
                else:
                    if moveNode.data < moveNodeParent.data:
                        moveNodeParent.left = None
                    else:
                        moveNodeParent.right = None
                return True


class BST(object):
    def __init__(self):
        self.root = None

    # return True if successfully inserted, false if exists
    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    # return True if d is found in tree, false otherwise
    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return False

    # return True if node successfully removed, False if not removed
    def remove(self, d):
        # Case 1: Empty Tree?
        if self.root == None:
            return False

        # Case 2: Deleting root node
        if self.root.data == d:
            # Case 2.1: Root node has no children
            if self.root.left is None and self.root.right is None:
                self.root = None
                return True
            # Case 2.2: Root node has left child
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
                return True
            # Case 2.3: Root node has right child
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
                return True
            # Case 2.4: Root node has two children
            else:
                moveNode = self.root.right
                moveNodeParent = None
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.root.data = moveNode.data
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
                return True
        # Find node to remove
        parent = None
        node = self.root
        while node and node.data != d:
            parent = node
            if d < node.data:
                node = node.left
            elif d > node.data:
                node = node.right
        # Case 3: Node not found
        if node == None or node.data != d:
            return False
        # Case 4: Node has no children
        elif node.left is None and node.right is None:
            if d < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        # Case 5: Node has left child only
        elif node.left and node.right is None:
            if d < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # Case 6: Node has right child only
        elif node.left is None and node.right:
            if d < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.right
            while moveNode.left:
                moveNodeParent = moveNode
                moveNode = moveNode.left
            node.data = moveNode.data
            if moveNode.right:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = moveNode.right
                else:
                    moveNodeParent.right = moveNode.right
            else:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
            return True


def serialize_bst(root):
    if root is None:
        return ""

    serialized = []

    def preorder_traversal(node):
        if node is None:
            serialized.append("#")
        else:
            serialized.append(str(node.data))
            preorder_traversal(node.left)
            preorder_traversal(node.right)

    preorder_traversal(root)
    return ",".join(serialized)


def deserialize_bst(serialized):
    bintree = BST()
    if not serialized:
        return None

    nodes = serialized.split(",")

    index = 0
    while True:
        if index >= len(nodes):
            return bintree
        elif nodes[index] == "#":
            index += 1
        else:
            value = nodes[index]
            bintree.insert(value)
            index += 1

class abstracttree:

    @abstractmethod
    def root(self):
        pass
    
    @abstractmethod
    def children(self,pos):
        pass

    @abstractmethod
    def parent(self,pos):
        pass

    @abstractmethod
    def num_children(self,pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def element(self):
        pass

    def isroot(self,pos):

        return self.root() == pos
    
    def isleaf(self,pos):
    
        return self.num_children(pos) == 0
    
    def isemtpy(self):

        return self.size == 0
    
    def depthN(self,pos):

        if self.isroot(pos):
            return 0

        return 1 + self.depthN(self.parent(pos))
    
    def heightN(self,pos):

        if self.isleaf(pos):

            return 0
        
        return 1 + max(self.heightN(child) for child in self.children(pos))
    
    def height(self,pos=None):

        if pos is None:

            return self.heightN(self.root())
        
        return self.heightN(pos)
    
    def depth(self,pos=None):

        if pos is None:

            return self.depthN(self.root())
        
        return self.depthN(pos)
    

class absbintree(abstracttree):

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

    def children(self,pos):

        children_list = []

        if pos.left() is not None:

            children_list.append(self.element(pos.left()))
        
        if pos.right() is not None:

            children_list.append(self.element(pos.right()))

        return children_list
    
    def sibling(self,pos):

        parent = self.parent(pos)
        if self.left(parent) == pos:
            return self.right(parent)
        
        return self.left(parent)


class BTNode:

        __slots__ = ['item','Tleft','Tright','parent']

        def __init__(self,item,Tleft,Tright,parent):

            self.item = item
            self.Tleft = Tleft
            self.Tright = Tright
            self.parent = parent

        def __setitem__(self,ele):

            self.item = ele

        def __getitem__(self):

            return self.item
        

class linkedbinarytree(absbintree):

    def __init__(self,item=None,Tleft=None,Tright=None,parent=None):
        
        self.Root = None
        self.size = None

        if item is not None:

            self.Root = self.addroot(item)
            self.size = 1

            if Tleft is not None:

                if Tleft.Root is not None:
                    
                    Tleft.Root.parent = self.Root
                    self.Root

class snode:

    __slots__ = ['item','next']

    def __init__(self,item=None,next=None):

        self.item = item
        self.next = next


class linkedls:

    def __init__(self):

        self.head = self.rear = snode()
        self.size = 0

    def append(self,ele):

        temp = snode(ele)
        self.rear.next = temp
        self.rear = temp
        self.size += 1

    def pop(self,pos=None):
            
        if self.isempty():

            raise Exception("Emtpy list")

        if pos is None:
            pos = self.findprev(self.rear)
            del_item = self.rear.item
            pos.next = None
            self.rear = pos
            self.size -= 1
            return del_item

        else:

            new = self.findprevind(pos)
            del_item = new.next.item
            new.next = new.next.next
            self.size -= 1
            return del_item

    def findprevind(self,ind):

        curpose = self.head
        count = 0

        while count < ind:

            curpose = curpose.next
            count += 1
        
        return curpose

    def findprev(self,pos):

        curpos = self.head

        while curpos.next is not pos:

            curpos = curpos.next
        
        return curpos
    
    def insert(self,ele,pos):

        prevpos = self.findprev(pos)
        temp = snode(ele)
        temp.next = pos
        prevpos.next = temp
        self.size += 1

    def isempty(self):

        return self.head == self.rear

    def find(self,ele):

        curpos = self.head

        while curpos.next.item is not ele:

            curpos = curpos.next
        
        return curpos
    
    def delete(self,ele):

        if self.isempty():
            raise Exception("empty list")

        curpos = self.find(ele)

        if self.rear != curpos:
            curpos.next = curpos.next.next
            self.size -= 1

        else:
            curpos.next = None
            self.size -= 1
            self.rear = curpos

    def __len__(self):

        return self.size
    
    def __str__(self):

        s = '['

        pos = self.head.next
        while pos is not None:

            s += str(pos.item) + ','
            pos = pos.next

        if s[-1] == ',':

            s = s[:-1]

        return s + ']'
    

a = linkedls()

# a.append(10)
# a.append(20)
# a.append(30)
# a.append(40)
# a.append(50)
# a.append(60)
# print(a)
# print(a.pop())
# print(a.pop())
# print(a)
# print(a.pop(1))
# print(a)
# a.delete(10)
# print(a)
# a.delete(40)
# print(a)

class linkedarr:

    def __init__(self):

        self.top = snode()
        self.size = 0

    def push(self,ele):
            
        if self.isempty():

            temp = snode(ele)
            self.top.next = temp
            self.size += 1

        else:

            temp = snode(ele)
            temp.next = self.top.next
            self.top.next = temp
            self.size += 1

    def pop(self):

        if self.isempty():

            raise Exception("Stack underflow")
        
        del_item = self.top.next.item
        self.top.next = self.top.next.next
        self.size -= 1
        return del_item

    def isempty(self):

        return self.top.next == None

    def __str__(self):

        s = '['

        pos = self.top.next
        while pos is not None:

            s += str(pos.item) + ','
            pos = pos.next

        if s[-1] == ',':

            s = s[:-1]

        return s + ']'
    
# a = linkedarr()
# a.push(10)
# a.push(20)
# a.push(30)
# a.push(40)
# a.push(50)
# print(a)
# print(a.pop())
# print(a.pop())
# print(a)

class linkedq:

    def __init__(self):

        self.front = self.rear = snode()
        self.size = 0

    def enqueue(self,ele):

        temp = snode(ele)
        self.rear.next = temp
        self.rear = temp
        self.size += 1

    def dequeue(self):

        if self.isempty():

            raise Exception("Empty queue")
        
        del_ele = self.front.next.item
        self.front.next = self.front.next.next
        self.size -= 1
        return del_ele
        
    def __str__(self):

        s = '['

        pos = self.front.next
        while pos is not None:

            s += str(pos.item) + ','
            pos = pos.next

        if s[-1] == ',':

            s = s[:-1]

        return s + ']'
    
    def isempty(self):

        return self.front == self.rear
    
# a = linkedq()
# a.enqueue(10)
# a.enqueue(20)
# a.enqueue(30)
# print(a)
# print(a.dequeue())
# print(a.dequeue())
# print(a)

class circularlinkq:

    def __init__(self):

        self.front = self.rear = snode()
        self.rear.next = self.front
        self.size = 0
    
    def enqueue(self,ele):

        pass

class dnode:

    __slots__ = ['item','next','prev']

    def __init__(self,item=None,next=None,prev=None):

        self.item = item
        self.next = next
        self.prev = prev

class doublinkedls:

    def __init__(self):

        self.head = self.tail = dnode()
        self.size = 0
    
    def append(self,ele):

        temp = dnode(ele)
        temp.prev = self.tail
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def pop(self):
        pass

class BTnode:

    __slots__ = ['item','Tleft','Tright','parent']

    def __init__(self,item=None,Tleft=None,Tright=None,Parent=None):

        self.item = item
        self.tleft = Tleft
        self.tright = Tright
        self.parent = Parent
    
    def __setitem__(self,ele):

        self.item = ele

    def __getitem__(self):

        return self.item
    

class abstree(ABC):

    @abstractmethod
    def root(self):
        raise Exception("Not implemented")
    
    @abstractmethod
    def children(self):
        pass

    @abstractmethod
    def numchildren(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def Parent(self):
        pass

    def isroot(self,pos):

        return self.root() == pos
    
    def isleaf(self,pos):

        return self.numchildren == 0
    
    def depthN(self,pos):

        if self.isroot(pos):

            return 0
        
        return 1 + self.depthN(self.Parent(pos))
    
    def heightN(self,pos):

        if self.isleaf(pos):

            return 0
        
        return 1 + max([self.heightN(child) for child in self.children(pos)])
    
    def isempty(self):

        return len(self) == 0
    
    def height(self):

        pos = self.root()

        return self.heightN(pos)
    
class absbintree(abstree):

    @abstractmethod
    def getleft(self,pos):
        pass

    @abstractmethod
    def getright(self,pos):
        pass

    def sibling(self,pos):

        parent = self.Parent(pos)
        if self.numchildren(parent) == 1:

            return None
        
        if self.getleft(parent) == pos:

            return self.getright(parent)
        
        return self.getleft(parent)
    
    def children(self,pos):

        if pos is None:
            return None

        if self.getleft(pos) is not None:
            yield self.getleft(pos)

        if self.getright(pos) is not None:
            yield self.getright(pos)
    
class linkedbintree(absbintree):

    def __init__(self,item=None,Tleft=None,Tright=None,Parent=None):

        self.Root = None
        self.size = 0

        if item is not None:

            if self.Root is None:
                self.Root = self.addroot(item)
                self.size = 1

            if Tleft is not None:

                if Tleft.root() is not None:

                    Tleft.Root.parent = self.Root

a = 'man'
b = 'amn'
c = 'nam'
print(hash(a) == hash(b))
print(hash(a) == hash(c))


class expressiontree(linkedbinarytree):

    def __init__(self, item=None, Tleft=None, Tright=None, parent=None):
        super().__init__(item, Tleft, Tright, parent)
    
    def cons(self,st):


        s = []
        for ch in st:

            if ch in '+-/*':

                right = s.pop()
                left = s.pop()
                s.append(expressiontree(ch,right,left))

a = []
b = 'ab+c/d*e+f-'

class BinaryExpressionTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__()
    
def infix_to_binary_expression_tree(expression):
    # Operator precedence dictionary
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    
    # Helper function to check if a token is an operator
    def is_operator(token):
        return token in ['+', '-', '*', '/']
    
    # Helper function to construct the binary expression tree
    def construct_expression_tree(tokens):
        if len(tokens) == 1:
            # Base case: create a leaf node with the operand value
            return BinaryExpressionTree(tokens[0])
        
        # Find the operator with the lowest precedence
        min_precedence = float('inf')
        min_precedence_operator = None
        for i in range(len(tokens) - 2, -1, -2):
            operator = tokens[i]
            if precedence[operator] < min_precedence:
                min_precedence = precedence[operator]
                min_precedence_operator = i
        
        # Create a subtree with the operator as the root
        operator = tokens[min_precedence_operator]
        tree = BinaryExpressionTree(operator)
        
        # Recursively construct the left and right subtrees
        tree.left = construct_expression_tree(tokens[:min_precedence_operator])
        tree.right = construct_expression_tree(tokens[min_precedence_operator + 1:])
        
        return tree
    
    # Tokenize the expression into a list of operands and operators
    tokens = []
    current_token = ""
    for char in expression:
        if char.isspace():
            continue
        elif is_operator(char):
            tokens.append(current_token)
            tokens.append(char)
            current_token = ""
        else:
            current_token += char
    tokens.append(current_token)
    
    # Construct the binary expression tree
    tree = construct_expression_tree(tokens)
    return tree

expression = "3 + 4 * 2 - 5"
tree = infix_to_binary_expression_tree(expression)
