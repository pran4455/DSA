
from abc import ABC,abstractmethod
class absree(ABC):

    @abstractmethod
    def Root(self):
        pass

    @abstractmethod
    def Parent(self,pos):
        pass

    @abstractmethod
    def iterchildren(self,pos):
        pass

    @abstractmethod
    def numchildren(self,pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def isroot(self,pos):
        return pos == self.Root()
    
    def isleaf(self,pos):
        return self.numchildren(pos) == 0

    def heightN(self,pos):

        if self.isleaf(pos):

            return 0
        
        return 1 + max([self.heightN(child) for child in self.iterchildren(pos)])
    
    def depthN(self,pos):

        if self.isroot(pos):

            return 0
        
        return 1 + self.depthN(self.Parent(pos))
    
    def isempty(self):
        return self.__len__() == 0
    
class absbinree(absree):

    @abstractmethod
    def Left(self,pos):
        pass

    @abstractmethod
    def Right(self,pos):
        pass

    def iterchildren(self,pos):

        if self.Left(pos) is not None:
            yield self.Left(pos)
        if self.Right(pos) is not None:
            yield self.Right(pos)
    
    def sibling(self,pos):

        parent = self.Parent(pos)
        if self.Left(parent) == pos:
            if self.Right(parent) is not None:
                return self.Right(parent)
        else:
            if self.Left(parent) is not None:
                return self.Left(parent)

class tnode:

    __slots__ = ['item','left','right','parent']
    def __init__(self,item=None,left=None,right=None,parent=None):

        self.item = item
        self.left = left
        self.right = right
        self.parent = parent

             
class linkbintree(absbinree):

    def __init__(self,item=None,tleft=None,tright=None,parent=None):

        self.root = None
        self.size = 0
        self.string = ''

        if item is not None:

            self.root = self.addroot(item)
            self.size = 1

            if tleft is not None:
                if tleft.root is not None:
                    tleft.parent = self.root
                    tleft.root = None
                    self.root.left = tleft
                    self.size += tleft.size
                else:
                    self.root.left = tnode(tleft)
            
            if tright is not None:
                if tright.root is not None:
                    tright.parent = self.root
                    tright.root = None
                    self.root.left = tright
                    self.size += tright.size
                else:
                    self.root.left = tnode(tright)
            
            if parent is not None:

                if self.root is None:
                    raise Exception("No root")
                else:
                    self.root.parent = parent
                    if parent.left is None:
                        parent.left = self.root
                        self.root = parent
                        self.size = parent.size
                    else:
                        parent.right = self.root
                        self.root = parent
                        self.size = parent.size
    
    def addroot(self,item):

        if self.root is not None:
            raise Exception("Root exists")
        
        self.root = tnode(item)
        self.size = 1
        return self.root
    
    def Parent(self, pos):
        return pos.parent
    
    def numchildren(self, pos):
        return len([child for child in self.iterchildren(pos)])
    
    def __len__(self):
        return self.size
    
    def Root(self):
        return self.root
    
    def preorder(self,pos,s=''):

        self.string += str(pos.item) + ','
        if pos.left is not None:
            self.preorder(pos.left,s)
        if pos.right is not None:
            self.preorder(pos.right,s)
    
    def postorder(self,pos,s=''):

        if pos.left is not None:
            self.postorder(pos.left,s)
        if pos.right is not None:
            self.postorder(pos.right,s)
        self.string += str(pos.item) + ','
    
    def inorder(self,pos,s=''):

        if pos.left is not None:
            self.inorder(pos.left, s)
        self.string += str(pos.item) + ','
        if pos.right is not None:
            self.inorder(pos.right, s)
    
    def makemirror(self,pos):

        if pos is None:
            return None

        mirrnode = tnode(pos.item)

        mirrnode.right = self.makemirror(pos.left)
        mirrnode.left = self.makemirror(pos.right)

        return mirrnode
    
    def mirror(self):

        return self.makemirror(self.root)
    
    def __str__(self) -> str:
        
        self.inorder(self.root)
        s = self.string
        self.string = ''
        return s
    
    def addLeft(self,item,pos=0):
        if pos == 0:
            pos = self.root
        pos.left = tnode(item,parent=pos)
        self.size += 1
    
    def addRight(self,item,pos=0):
        if pos == 0:
            pos = self.root
        pos.right = tnode(item,parent=pos)
        self.size += 1
    
    def Left(self, pos):
        return pos.left
    
    def Right(self, pos):
        return pos.right

class binsertree(linkbintree):

    def __init__(self, item=None, tleft=None, tright=None, parent=None):
        super().__init__(item, tleft, tright, parent)
    
    def append(self,item,pos=None):

        if pos is None:
            if self.isempty():
                self.addroot(item)
                return None
            else:
                pos = self.root

        if item > pos.item:
            if self.Right(pos) is None:
                return self.addRight(item,pos)
            else:
                return self.append(item,pos.right)
        if item < pos.item:
            if self.Left(pos) is None:
                return self.addLeft(item,pos)
            else:
                return self.append(item,pos.left)
    
    def findmin(self,pos = 0):
        if pos ==0:
            pos = self.root
        
        if pos.left is None:
            return pos.item
        else:
            return self.findmin(pos.left)
    
    def findmax(self,pos = 0):
        if pos ==0:
            pos = self.root
        
        if pos.right is None:
            return pos.item
        else:
            return self.findmax(pos.right)
    
    def findminnode(self,pos):

        if pos.left is None:
            return pos
        else:
            return self.findminnode(pos.left)
        
    def delete(self,item,pos=0):

        if pos == 0:
            pos = self.root
        
        if pos is None:
            return None
        
        if item == pos.item:

            if self.isleaf(pos):

                if self.isroot(pos):
                    self.root = None
                    
                parent = pos.parent
                if parent.left == pos:
                    parent.left = None
                    
                else:
                    parent.right = None
                    

            elif self.Left(pos) is None or self.Right(pos) is None:
                if self.Left(pos) is None:
                    child = self.Right(pos)
                else:
                    child = self.Left(pos)
                if pos == self.Root():
                    self.root = child
                else:
                    parent = self.Parent(pos)
                    if self.Left(parent) == pos:
                        parent.left = child
                    else:
                        parent.right = child

            else:
                minnode = self.findminnode(pos.right)
                pos.item = minnode.item
                self.delete(pos.item,pos.right)
        
        elif item < pos.item:
            return self.delete(item,pos.left)
        else:
            return self.delete(item,pos.right)
    
    def rightrotate(self,pos):

        parent = pos.parent
        if parent.right == pos:
            l = 0
            lchild = parent.left
        gp = parent.parent
        
import ctypes       
class Listadt:

    def __init__(self,cap):
        self.size = 0
        self.cap = cap
        self.arr = self.makearray(cap)
    
    def makearray(self,cap):

        b = (cap * ctypes.py_object)()
    
    def resize(self,size):

        arr = self.makearray(size)
        for i in range(self.size):
            arr[i] = self.arr[i]
        return arr

    def __setitem__(self,item,pos):

        self.arr[pos] = item
    
    def __getitem__(self,pos):

        return self.arr[pos]
    
    def append(self,item):

        if self.isfull():
            self.arr = self.resize(self.cap*2)

        self.arr[self.size] = item
        self.size += 1
    
    def pop(self,item):

        self.arr[self.size-1] = (ctypes.py_object)()
    
    def isfull(self):
        return self.size == self.cap
    
    def insert(self,item,pos):

        if self.isfull():
            self.arr = self.resize(self.cap*2)
        
        for i in range(self.size,pos,-1):

            self.arr[i] = self.arr[i-1]
        
        self.arr[pos] = item
    
    def delete(self,pos):

        for i in range(pos,self.size):
            self.arr[i] = self.arr[i+1]
    
    


if __name__ == "__main__":
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    
    binary_search_tree = binsertree()
    binary_search_tree.append(30)
    binary_search_tree.append(90)
    binary_search_tree.append(70)
    binary_search_tree.append(40)
    
    binary_search_tree.append(88)
    binary_search_tree.append(44)
    binary_search_tree.append(8)
    binary_search_tree.append(12)
    binary_search_tree.append(44)
    print(binary_search_tree)
    binary_search_tree.delete(88)
    print(binary_search_tree)
    binary_search_tree.delete(90)
    print(binary_search_tree)
    binary_search_tree.delete(30)
    print(binary_search_tree)
    print(binary_search_tree.findmax())
    print(binary_search_tree.findmin())
    print(binary_search_tree.rightRotate(binary_search_tree.Root()))
