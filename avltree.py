from abc import ABC
from abc import abstractmethod

class abstractTree(ABC):

    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self):
        pass

    @abstractmethod
    def iter_children(self,pos):
        pass

    @abstractmethod
    def numchildren(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def isroot(self,pos):

        return self.root() == pos
    
    def isleaf(self,pos):

        return self.numchildren(pos) == 0
    
    def depthN(self,pos):

        if self.isroot(pos):
            return 0
        
        return 1 + self.depthN(self.parent())
    
    def depth(self,pos=0):

        if pos == 0:
            pos = self.root()
        
        return self.depthN(pos)
    
    def heightN(self,pos):

        if self.isleaf(pos):
            return 0
        
        return 1 + max([self.heightN(child) for child in self.iter_children(pos)])
    
class abstractbinarytree(abstractTree):

    @abstractmethod
    def Left(self):
        pass

    @abstractmethod
    def Right(self):
        pass

    def sibling(self,pos):

        parent = self.parent(pos)
        if self.Left(parent) == pos:
            return self.Right(parent)
        elif self.Right(parent) == pos:
            return self.Left(parent)
    
    def iter_children(self,pos):
        
        if self.Left(pos) is not None:
            yield self.Left(pos)

        if self.Right(pos) is not None:
            yield self.Right(pos)

class avlnode:

    __slots__ = ['item','height','left','right','parent']

    def __init__(self,item=None,height=0,left=None,right=None,parent=None) -> None:
        
        self.item = item
        self.height = height
        self.left = left
        self.right = right
        self.parent = parent

class avltree(abstractbinarytree):
    
    def __init__(self):
        
        self.Root = None
        self.size = 0

    def addroot(self,item):

        if self.root() is not None:
            raise Exception("Root exists")
        
        rootnode = avlnode(item,height=0)
        self.Root = rootnode
        self.size = 1
        return self.Root
    
    def addLeft(self,item,pos):

        temp = avlnode(item)
        pos.left = temp
        pos2 = pos
        pos = pos.parent

        while pos.parent is not None:

            pos.height += 1
            pos = pos.parent

        return self.restructure(pos2)
    
    def addRight(self,item,pos):

        temp = avlnode(item)
        pos.right = temp
        pos2 = pos
        pos = pos.parent

        while pos.parent is not None:

            pos.height += 1
            pos = pos.parent

        return self.restructure(pos2)

    def append(self, ele, pos=None):
        if pos is None:
            if self.isEmpty():
                self.addroot(ele)
                return None
            else:
                pos = self.getRoot()

        if ele < pos.item:
            if self.Left(pos) is None:
                return self.addLeft(ele, pos)
            else:
                return self.append(ele, self.Left(pos))
        elif ele > pos.item:
            if self.Right(pos) is None:
                return self.addRight(ele, pos)
            else:
                return self.append(ele, self.Right(pos))
        else:
            return None
   
    def findmin(self,pos=0):

        if pos == 0:
            pos = self.getRoot()

        if pos.left is not None:

            return self.findmin(pos.left)
        
        else:

            return pos.item
        
    def findmax(self,pos=0):

        if pos == 0:
            pos = self.getRoot()

        if pos.right is not None:

            return self.findmax(pos.right)
        
        else:

            return pos.item
        
    def all_children(self,pos):

        l = [childr.item for childr in self.getChildren(pos)]
        return l

    def delete(self, ele, pos=0):
        if pos is 0:
            pos = self.getRoot()

        if pos is None:
            return None 

        if ele < pos.item:
            self.delete(ele, self.Left(pos))
        elif ele > pos.item:
            self.delete(ele, self.Right(pos))
        else:
            if self.isLeaf(pos):  
                if pos == self.getRoot():
                    self.Root = None
                else:
                    parent = self.getParent(pos)
                    if self.Left(parent) == pos:
                        parent.left = None
                    else:
                        parent.right = None
            elif self.Left(pos) is None or self.Right(pos) is None:
                if self.Left(pos) is None:
                    child = self.Right(pos)
                else:
                    child = self.Left(pos)
                if pos == self.getRoot():
                    self.root = child
                else:
                    parent = self.getParent(pos)
                    if self.Left(parent) == pos:
                        parent.left = child
                    else:
                        parent.right = child
            else:  
                min_node = self.getminNode(self.Right(pos))
                pos.item = min_node.item
                self.delete(min_node.item, self.Right(pos))

    def __contains__(self,pos,ele):

        if pos == None:
            return False

        if ele < pos.item:
            return self.__contains__(pos.left,ele)
        
        elif ele > pos.item:
            return self.__contains__(pos.right,ele)
        
        elif ele == pos.item:
            return True
        
    def restructure(self,pos1,pos=0):

        if pos == 0:
            pos = self.root()

        if pos == None:
            return None

        if pos.left.height - pos.right.height not in [-1,0,1]:

            if pos1 in pos.left.left:

                return self.clockrot(pos,pos1)

            if pos1 in pos.left.right:

                self.clockrot(pos.left,pos1)
                return self.anticlockrot(pos,pos.left)

            if pos1 in pos.right.left:

                return self.anticlockrot(pos,)



            if pos1 in pos.right.right: