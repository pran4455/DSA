from abc import abstractmethod
from abc import ABC


class AbstractTree(ABC):
    @abstractmethod
    def getRoot(self):
        """Returns the root position of the tree."""
        raise Exception("Not implemented")

    @abstractmethod
    def getParent(self, pos):
        """Returns the parent position of the given position 'pos'."""
        raise Exception("Not implemented")

    @abstractmethod
    def getNum_children(self, pos):
        """Returns the number of children of the given position 'pos'."""
        raise Exception("Not implemented")

    @abstractmethod
    def getChildren(self, pos):
        """Returns a list of children positions of the given position 'pos'."""
        raise Exception("Not implemented")

    @abstractmethod
    def __len__(self):
        """Returns the total number of positions in the tree."""
        raise Exception("Not implemented")

    def isRoot(self, pos):
        """Returns True if the given position 'pos' is the root of the tree, False otherwise."""
        return self.getRoot() == pos

    def isLeaf(self, pos):
        """Returns True if the given position 'pos' is a leaf node (has no children), False otherwise."""
        return self.getNum_children(pos) == 0

    def isEmpty(self):
        """Returns True if the tree is empty (has no positions), False otherwise."""
        return len(self) == 0

    def depthN(self, pos):
        """
        Returns the depth of the position 'pos' in the tree.
        Depth is the number of edges in the path from the root to 'pos'.
        """
        if self.isRoot(pos):
            return 0
        return 1 + self.depthN(self.getParent(pos))

    def heightN(self, pos):
        """
        Returns the height of the position 'pos' in the tree.
        Height is the number of edges in the longest path from 'pos' to a leaf.
        """
        if self.isLeaf(pos):
            return 0
        return 1 + max([self.heightN(child) for child in self.getChildren(pos)])

    def height(self):
        """Returns the height of the tree (i.e., the height of the root position)."""
        return self.heightN(self.getRoot())


class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def getLeft(self, pos):
        raise Exception("Not implemented")

    @abstractmethod
    def getRight(self, pos):
        raise Exception("Not implemented")

    def getChildren(self, pos):
        if pos is None:
            return None
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)

    def sibling(self, pos):
        parent = self.getParent(pos)
        if parent is None:
            return None
        if pos == self.right(parent):
            return self.left(parent)
        else:
            return self.right(parent)


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
        pass

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
        self.string = "The preorder is: "
        self.preorder(self.root)
        self.string = self.string[:-1]
        self.string += "\nThe inorder is: "
        self.inorder(self.root)
        self.string = self.string[:-1]
        self.string += "\nThe postorder is: "
        self.postorder(self.root)
        self.string = self.string[:-1]
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

        mirnode = self.BTNode(pos.item)
        mirnode.right = self.makeMirror(pos.left)
        mirnode.left = self.makeMirror(pos.right)

        return mirnode

    def mirror(self):
        mirrtree = LinkedBinaryTree()
        mirrtree.root = mirrtree.makeMirror(self.getRoot())
        return mirrtree

#driver code
if __name__ == "__main__":
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    tree = LinkedBinaryTree()
    tree.addRoot("a")
    tree.addLeft("b")
    tree.addRight("c")
    tree.addRight("d",tree.root.right)
    tree.addRight("e",tree.root.right.right)

    print(tree)
    print()

    print(tree.mirror())
