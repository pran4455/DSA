from binarytree import AbstractTree
from abc import ABC
from abc import abstractmethod


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


class DecisionTree(AbstractTree):
    """
    Implementation of a decision tree using the AbstractTree ADT.

    Each node in the decision tree represents a feature, rule, and label combination.
    The tree can be constructed by adding nodes to the root and connecting them using
    the addRoot and addNode methods.

    Attributes:
        TreeNode: An inner class representing a node in the decision tree.
            Contains the feature, rule, label, and a list of child nodes.

    Methods:
        addRoot(feature, rule, label):
            Adds the root node to the decision tree.
            Returns the root node position.

        addNode(parent, feature, rule, label):
            Adds a new node to the decision tree as a child of the given parent node.
            Returns the new node position.

        getRoot():
            Returns the root position of the decision tree.

        getParent(pos):
            Returns the parent position of the given node position.

        getNum_children(pos):
            Returns the number of children of the given node position.

        getChildren(pos):
            Returns a list of children positions of the given node position.

        __len__():
            Returns the total number of positions in the decision tree.

        getFeature(pos):
            Returns the feature associated with the given node position.

        getRule(pos):
            Returns the rule associated with the given node position.

        getLabel(pos):
            Returns the label associated with the given node position.

        printTree(pos=None, indent=0):
            Prints the decision tree starting from the given node position.
            Uses indentation to represent the tree structure.
    """

    class TreeNode:
        """
        Represents a node in the decision tree.

        Attributes:
            feature: The feature associated with the node.
            rule: The rule associated with the node.
            label: The output label associated with the node.
            children: A list of child nodes.
        """

        def __init__(self, feature=None, rule=None, label=None):
            self.feature = feature
            self.rule = rule
            self.label = label
            self.children = []

    def __init__(self):
        """
        Initializes a new instance of the DecisionTree class.
        """
        self.root = None
        self.size = 0

    def addRoot(self, feature, rule, label):
        """
        Adds the root node to the decision tree.

        Args:
            feature: The feature associated with the root node.
            rule: The rule associated with the root node.
            label: The output label associated with the root node.

        Returns:
            The root node position.
        """
        if self.root is not None:
            raise ValueError("Root already exists")
        else:
            self.root = self.TreeNode(feature, rule, label)
            self.size += 1
            return self.root

    def addNode(self, parent, feature, rule, label):
        """
        Adds a new node to the decision tree as a child of the given parent node.

        Args:
            parent: The parent node position.
            feature: The feature associated with the new node.
            rule: The rule associated with the new node.
            label: The output label associated with the new node.

        Returns:
            The new node position.
        """
        node = self.TreeNode(feature, rule, label)
        parent.children.append(node)
        self.size += 1
        return node

    def getRoot(self):
        """
        Returns the root position of the decision tree.

        Returns:
            The root position of the decision tree.
        """
        return self.root

    def getParent(self, pos):
        """
        Returns the parent position of the given node position.

        Args:
            pos: The node position.

        Returns:
            The parent position of the given node position.
        """
        if pos is self.root:
            return None
        else:
            return self.find_parent(self.root, pos)

    def find_parent(self, current_node, pos):
        """
        Helper method to find the parent node position recursively.

        Args:
            current_node: The current node being examined.
            pos: The node position to find its parent.

        Returns:
            The parent position of the given node position.
        """
        for child in current_node.children:
            if child is pos:
                return current_node
            else:
                parent = self.find_parent(child, pos)
                if parent is not None:
                    return parent
        return None

    def getNum_children(self, pos):
        """
        Returns the number of children of the given node position.

        Args:
            pos: The node position.

        Returns:
            The number of children of the given node position.
        """
        return len(pos.children)

    def getChildren(self, pos):
        """
        Returns a list of children positions of the given node position.

        Args:
            pos: The node position.

        Returns:
            A list of children positions of the given node position.
        """
        return pos.children

    def __len__(self):
        """
        Returns the total number of positions in the decision tree.

        Returns:
            The total number of positions in the decision tree.
        """
        return self.size

    def getFeature(self, pos):
        """
        Returns the feature associated with the given node position.

        Args:
            pos: The node position.

        Returns:
            The feature associated with the given node position.
        """
        return pos.feature

    def getRule(self, pos):
        """
        Returns the rule associated with the given node position.

        Args:
            pos: The node position.

        Returns:
            The rule associated with the given node position.
        """
        return pos.rule

    def getLabel(self, pos):
        """
        Returns the label associated with the given node position.

        Args:
            pos: The node position.

        Returns:
            The label associated with the given node position.
        """
        return pos.label

    def printTree(self, pos=None, indent=0):
        """
        Prints the decision tree starting from the given node position.

        Args:
            pos: The starting node position (default: root node).
            indent: The indentation level (default: 0).
        """
        if pos is None:
            pos = self.root

        print(
            "  " * indent
            + f"Feature: {pos.feature}, Rule: {pos.rule}, Label: {pos.label}"
        )
        for child in pos.children:
            self.printTree(child, indent + 1)


# driver code
if __name__ == "__main__":
    # this part of the code will only be run when the function is called directly
    # it will not be executed when it is imported as a module

    tree = DecisionTree()

    root_node = tree.addRoot("Patron", "Is a patron", "Yes/No")
    n1 = tree.addNode(root_node, "Hungry", "Full or not full", "Yes/no")
    n2 = tree.addNode(n1, "Type", "dish", "Yes")
    n3 = tree.addNode(n2, "Food", "French", "Yes")
    n4 = tree.addNode(n2, "Food", "Italian", "No")
    n5 = tree.addNode(n2, "Food", "Burger", "Yes")
    n6 = tree.addNode(n2, "day", "Friday/Saturday", "Yes")

    tree.printTree()
