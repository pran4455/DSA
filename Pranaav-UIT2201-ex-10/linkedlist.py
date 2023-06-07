
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


    def __init__(self):

        '''
        SinglyLinkedList class represents a singly linked list.

        Initializes an empty list with a head and tail node.

        '''


        self.head = self.tail = Node()


    def isempty(self):

        '''
        Checks if the linked list is empty.

        Returns:
            True if the linked list is empty, False otherwise.

        '''

        return self.head == self.tail
    

    def append(self,ele):

        temp = Node(ele)
        self.tail.next = temp
        self.tail = temp


    def __str__(self):

        pos = self.head.next
        s = '['

        while pos is not None:
            s += str(pos.item) + ','
            pos = pos.next

        s.rstrip(',')

        return s + ']'
    

    def find(self,ele):

        pos = self.head.next
        ct = 0

        while pos is not None:
            
            if pos.item == ele:

                return ct
            
            ct += 1
            pos = pos.next
            
        return -1
    

    def __contains__(self,ele):

        pos = self.head.next
        ct = 0

        while pos is not None:
            
            if pos.item == ele:

                return True
            
            ct += 1
            pos = pos.next
            
        return False
    
    def a(self):

        return self.head.next.item
    

    def findprev(self,ind):

        pos = self.head.next

        for i in range(ind-1):

            pos = pos.next

        return pos

    def pop(self,ind):

        pos = self.findprev(ind)
        self.tail.next = pos
        self.tail = pos.next.next


        
a = SinglyLinkedList()
a.append(5)
a.append(6)
a.append(8)
print(a.pop(1))
print(a)