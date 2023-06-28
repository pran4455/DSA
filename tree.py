from abc import ABCMeta, abstractmethod

class AbstractTree(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def rootnode(self):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def children(self, node):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def numofchildren(self, node):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def parent(self, node):
        raise NotImplementedError("method not implemented")
    
    def depth(self, node):
        
        if node == self.is_rootnode():
            return 0
        
        return 1 + self.depth(self.parent(node))
    
    
    def height(self, node):
        
        if node == self.is_leaf():
            return 0
        
        return 1 + max(self.height(child) for child in self.children(node))
    
    def is_leaf(self, node):
        
        return self.numofchildren(node) == 0
    
    def is_rootnode(self, node):

        return self.rootnode() == node
    
    def isempty(self):

        return len(self) == 0
    

class AbstractBinaryTree(AbstractTree):

    @abstractmethod
    def left(self, node):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def right(self, node):
        raise NotImplementedError("method not implemented")
    
    def children(self, node):
        
        if node is None:

            return None
        
        if self.left(node) is not None:

            yield self.left(node)

        if self.right(node) is not None:

            yield self.right(node)

    def sibling(self, node):

        parent = self.parent(node)
        if self.left(parent) == node:
            return self.right(parent)
        return self.left(parent)
        

class BinaryTree(AbstractBinaryTree):

    class BTNode:

        __slots__ = ['item','left','right','parent']


        def __init__(self,item=None,left=None,right=None,parent=None):

           self.item = item
           self.left = left
           self.right = right
           self.parent = parent
 

    def __init__(self,item=None, left=None, right=None, parent=None):

        self.root = None
        self.size = 0
        if item is not None:
            self.root = self.addroot(item)
            if left is not None:
                if left.root is not None:
                    left.root.parent = self.root
                    self.root.left = self.left(left.root)
                    self.size += left.size
                    

    def rootnode(self,pos):
        
        if pos is not None:
            self.root = pos
    
    def addroot(self,node):

        if self.root is not None:

            raise Exception("Root already exists")
        
        
