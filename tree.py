from abc import ABCMeta, abstractmethod

class AbstractTree(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def root(self):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def children(self, node):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def num_children(self, node):
        raise NotImplementedError("method not implemented")
    
    @abstractmethod
    def parent(self, node):
        raise NotImplementedError("method not implemented")
    
    def depth(self, node):
        
        if node == self.is_root():
            return 0
        
        return 1 + self.depth(self.parent(node))
    

    def height(self, node):
        
        if node == self.is_leaf():
            return 0
        
        return 1 + max(self.height(child) for child in self.children(node))
    
    def is_leaf(self, node):
        
        return self.num_children(node) == 0
    
    def is_root(self, node):

        return self.root() == node
    
    def isempty(self):

        return len(self) == 0
    
    
    def preorder(self,pos,s):

        s += str(pos.item) + ','

        if pos.left is not None:

            return self.preorder(self.left,s)
        
        if pos.right is not None:

            return self.preorder(self.right,s)
        

    def __str__(self):

        s = ''
        self.preorder(self.root,s)
        return s
    

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

    def num_children(self, node):
        
        if node is None:
            return 0
        
        if self.left(node) is not None:
            return 1
        
        if self.right(node) is not None:
            return 1
        
        return 0

    def sibling(self, node):

        parent = self.parent(node)
        if self.left(parent) == node:
            return self.right(parent)
        return self.left(parent)


class BTNode:

        __slots__ = ['item','left','right','parent']


        def __init__(self,item=None,left=None,right=None,parent=None):

           self.item = item
           self.left = left
           self.right = right
           self.parent = parent

        def __setitem__(self,ele):

            self.item = ele

        def __getitem__(self):

            return self.item


# class BinaryTree(AbstractBinaryTree):

#     def __init__(self,item=None, left=None, right=None, parent=None):

#         self.rootnode = None
#         self.size = 0
#         if item is not None:
#             self.rootnode = self.addroot(item)

#             if left is not None:

#                 if left.rootnode is not None:
#                     left.root.parent = self.rootnode
#                     self.rootnode.left = self.left(left.root)
#                     self.size += left.size

#             if right is not None:
#                 if right.rootnode is not None:
#                     right.root.parent = self.rootnode
#                     self.rootnode.right = self.right(right.root)
#                     self.size += right.size
                    

#     def root(self,pos):
        
#         return self.root
    
#     def addroot(self,item):

#         if self.rootnode is not None:

#             raise Exception("Root already exists")
        
#         self.rootnode = BTNode(item)
#         self.size = 1
#         return self.rootnode
    
#     def parent(self,pos):

#         if pos == self.is_root:

#             raise Exception("Position is root")
        
#         return pos.parent
    
#     def left(self, node):
#         return node.left
    
#     def right(self, node):
#         return node.right
    
#     def __len__(self):
#         return self.size
    
    
#     def addLeft(self, item, pos=None):
#         if pos is None:
#             pos = self.root
#         if self.left(pos) is not None:
#             raise ValueError("Left child already exists")
#         else:
#             pos.left = self.BTNode(item, parent=pos)
#             self.size += 1
#             return pos.left

#     def addRight(self, item, pos=None):
#         if pos is None:
#             pos = self.root
#         if self.right(pos) is not None:
#             raise ValueError("Right child already exists")
#         else:
#             pos.right = self.BTNode(item, parent=pos)
#             self.size += 1
#             return pos.right

# class LinkedBinaryTree(AbstractBinaryTree):
#     class BTNode:
#         __slots__ = ["item", "left", "right", "parent"]

#         def __init__(self, item, left=None, right=None, parent=None):
#             self.item = item
#             self.left = left
#             self.right = right
#             self.parent = parent

#         def getitem(self):
#             return self.item

#         def setitem(self, item):
#             self.item = item

#     __slots__ = ["root", "size"]

#     def __init__(self, item=None, t_left=None, t_right=None, parent=None):
#         self.root = None
#         self.size = 0
#         self.string = ""
#         self.parent = parent
#         if item is not None:
#             self.root = self.addRoot(item)
#         if t_left is not None:
#             if t_left.root is not None:
#                 t_left.root.parent = self.root
#                 self.root.left = t_left.root
#                 self.size += t_left.size
#                 t_left.root = None
#         if t_right is not None:
#             if t_right.root is not None:
#                 t_right.root.parent = self.root
#                 self.root.right = t_right.root
#                 self.size += t_right.size
#                 t_right.root = None

#     def addRoot(self, item):
#         if self.root is not None:
#             raise ValueError("Root already exists")
#         else:
#             self.root = self.BTNode(item)
#             self.size += 1
#             return self.root

#     def __len__(self):
#         return self.size

#     def getParent(self, pos):
#         return pos.parent

#     def getLeft(self, pos):
#         return pos.left

#     def getRight(self, pos):
#         return pos.right

#     def getRoot(self):
#         return self.root

#     def getSize(self):
#         return self.size

#     def getNum_children(self, pos):
#         if pos is None:
#             return 0
#         else:
#             return 1 + self.getNum_children(pos.left) + self.getNum_children(pos.right)

#     def addLeft(self, item, pos=None):
#         if pos is None:
#             pos = self.root
#         if self.getLeft(pos) is not None:
#             raise ValueError("Left child already exists")
#         else:
#             pos.left = self.BTNode(item, parent=pos)
#             self.size += 1
#             return pos.left

#     def addRight(self, item, pos=None):
#         if pos is None:
#             pos = self.root
#         if self.getRight(pos) is not None:
#             raise ValueError("Right child already exists")
#         else:
#             pos.right = self.BTNode(item, parent=pos)
#             self.size += 1
#             return pos.right

#     def preorder(self, pos):
#         self.string += str(pos.item) + ","
#         if pos.left is not None:
#             self.preorder(pos.left)
#         if pos.right is not None:
#             self.preorder(pos.right)

#     def postorder(self, pos):
#         if pos.left is not None:
#             self.preorder(pos.left)
#         if pos.right is not None:
#             self.preorder(pos.right)
#         self.string += str(pos.item) + ","

#     def inorder(self, pos):
#         if pos.left is not None:
#             self.preorder(pos.left)
#         self.string += str(pos.item) + ","
#         if pos.right is not None:
#             self.preorder(pos.right)

#     def __str__(self):
#         self.string = "Preorder: "
#         self.preorder(self.root)
#         self.string += "|Inorder: "
#         self.inorder(self.root)
#         self.string += "|Postorder: "
#         self.postorder(self.root)
#         self.string += "|"
#         return self.string


class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode:
        __slots__ = ["item", "left", "right", "parent"]

        def __init__(self, item, left=None, right=None, parent=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

        def getitem(self):
            return self.item

        def setitem(self, item):
            self.item = item

    __slots__ = ["root", "size"]

    def __init__(self, item=None, t_left=None, t_right=None):
        self.root = None
        self.size = 0
        self.string = ""
        if item is not None:
            self.root = self.addRoot(item)
        if t_left is not None:
            if t_left.root is not None:
                t_left.root.parent = self.root
                self.root.left = t_left.root
                self.size += t_left.size
                t_left.root = None
        if t_right is not None:
            if t_right.root is not None:
                t_right.root.parent = self.root
                self.root.right = t_right.root
                self.size += t_right.size
                t_right.root = None

    def addRoot(self, item):
        """
        Adds a root node with the given item to the tree.

        Args:
            item: The item to be stored in the root node.

        Returns:
            The root position of the added node.

        Raises:
            ValueError: If the root already exists.
        """
        if self.root is not None:
            raise ValueError("Root already exists")
        else:
            self.root = self.BTNode(item)
            self.size += 1
            return self.root

    def __len__(self):
        """
        Returns the number of nodes in the tree.

        Returns:
            The size of the tree.
        """
        return self.size

    def getParent(self, pos):
        """
        Returns the parent position of the given position 'pos'.

        Args:
            pos: The position to get the parent of.

        Returns:
            The parent position of 'pos'.
        """
        return pos.parent

    def getLeft(self, pos):
        """
        Returns the left child position of the given position 'pos'.

        Args:
            pos: The position to get the left child of.

        Returns:
            The left child position of 'pos'.
        """
        return pos.left

    def getRight(self, pos):
        """
        Returns the right child position of the given position 'pos'.

        Args:
            pos: The position to get the right child of.

        Returns:
            The right child position of 'pos'.
        """
        return pos.right

    def getRoot(self):
        """
        Returns the root position of the tree.

        Returns:
            The root position.
        """
        return self.root

    def getSize(self):
        """
        Returns the number of nodes in the tree.

        Returns:
            The size of the tree.
        """
        return self.size

    def getNum_children(self, pos):
        """
        Returns the number of children of the given position 'pos'.

        Args:
            pos: The position to get the number of children of.

        Returns:
            The number of children of 'pos'.
        """
        if pos is None:
            return 0
        else:
            return 1 + self.getNum_children(pos.left) + self.getNum_children(pos.right)

    def addLeft(self, item, pos=None):
        """
        Adds a left child node with the given item to the specified position 'pos' or the root if 'pos' is None.

        Args:
            item: The item to be stored in the left child node.
            pos: The position to add the left child to. If None, the left child is added to the root.

        Returns:
            The position of the added left child node.

        Raises:
            ValueError: If the left child already exists.
        """
        if pos is None:
            pos = self.root
        if self.getLeft(pos) is not None:
            raise ValueError("Left child already exists")
        else:
            pos.left = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.left

    def addRight(self, item, pos=None):
        """
        Adds a right child node with the given item to the specified position 'pos' or the root if 'pos' is None.

        Args:
            item: The item to be stored in the right child node.
            pos: The position to add the right child to. If None, the right child is added to the root.

        Returns:
            The position of the added right child node.

        Raises:
            ValueError: If the right child already exists.
        """
        if pos is None:
            pos = self.root
        if self.getRight(pos) is not None:
            raise ValueError("Right child already exists")
        else:
            pos.right = self.BTNode(item, parent=pos)
            self.size += 1
            return pos.right

    def preorder(self, pos):
        """
        Performs a preorder traversal starting from the given position 'pos'.

        Args:
            pos: The starting position for the preorder traversal.
        """
        self.string += str(pos.item) + ","
        if pos.left is not None:
            self.preorder(pos.left)
        if pos.right is not None:
            self.preorder(pos.right)

    def postorder(self, pos):
        """
        Performs a postorder traversal starting from the given position 'pos'.

        Args:
            pos: The starting position for the postorder traversal.
        """
        if pos.left is not None:
            self.postorder(pos.left)
        if pos.right is not None:
            self.postorder(pos.right)
        self.string += str(pos.item) + ","

    def inorder(self, pos):
        """
        Performs an inorder traversal starting from the given position 'pos'.

        Args:
            pos: The starting position for the inorder traversal.
        """
        if pos.left is not None:
            self.inorder(pos.left)
        self.string += str(pos.item) + ","
        if pos.right is not None:
            self.inorder(pos.right)

    def __str__(self):
        """
        Returns a string representation of the tree by performing preorder, inorder, and postorder traversals.

        Returns:
            A string representation of the tree.
        """
        self.string = "Preorder: "
        self.preorder(self.root)
        self.string += "|Inorder: "
        self.inorder(self.root)
        self.string += "|Postorder: "
        self.postorder(self.root)
        self.string += "|"
        return self.string

    def makeMirror(self, pos=None):
        """
        Constructs a new binary tree representing the mirror image of the original tree.

        Args:
            pos: The position to start the mirror operation. If None, starts from the root.

        Returns:
            The root position of the new mirror tree.
        """
        if pos is None:
            pos = self.root

        if pos is None:
            return None

        # Create a new node with the same item
        mirror_node = self.BTNode(pos.item)

        # Construct the mirror image of the left and right subtrees and assign them as right and left children,
        # respectively
        mirror_node.right = self.makeMirror(pos.left)
        mirror_node.left = self.makeMirror(pos.right)

        return mirror_node

    def mirror(self):
        mirrored_tree = LinkedBinaryTree()
        mirrored_tree.root = mirrored_tree.makeMirror(self.getRoot())
        return mirrored_tree

tree = LinkedBinaryTree()
tree.addRight("f")
tree.addRight("g")
tree.addRight("h")
tree.addRight("i")