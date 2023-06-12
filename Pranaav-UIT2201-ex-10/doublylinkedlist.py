class Node:

    __slots__ = ['item', 'next', 'prev']

    def __init__(self,item=None,next=None,prev=None):

        '''
        Node class represents a node in a singly linked list.

        Args:
            item: The item/value stored in the node.
            next: Reference to the next node.

        '''

        self.item = item
        self.next = next
        self.prev = prev

class doublylinkedlist:

    def __init__(self):

        self.head = self.tail = Node()
        self.size = 0

    def append(self, ele):

        temp = Node(ele)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1
    
    def insert(self, ind, ele):

        if ind > 0 and ind < self.size-2:

            pos = self.findprev(ind)
            temp = Node(ele)
            pos.next.prev = temp
            temp.next = pos.next
            pos.next = temp
            temp.prev = pos
            self.size += 1

        elif ind == self.size - 1:

            self.append(ele)

        else:
            raise Exception("Invalid index")
        

    def findprev(self,ind):

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

        pos = self.tail
        s = '['

        while pos is not None and pos.item is not None:
            s += str(pos.item) + ','
            pos = pos.prev

        if s[-1] == ',':
            s = s[:-1]

        return s + ']'
    
    def pop(self,ind=None):

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

        return self.size


a = doublylinkedlist()
a.append(10)
a.append(20)
a.append(30)
a.append(40)
a.append(50)
a.append(60)
a.insert(1,10000)
print(a)
a.insert(1,20000)
print(a)
a.insert(1,30000)
print(a)
a.insert(1,40000)
print(a)
print(a.pop(2))
print(a)
print(a.pop(2))
print(a)
print(a.pop(2))
print(a)
print(a.reverse_display())
