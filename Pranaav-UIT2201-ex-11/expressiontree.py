from binarytree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):

    def __init__(self, item=None, t_left=None, t_right=None):
        super().__init__(item, t_left, t_right)

    def constructbinarytree(self, string):
        """
        constructbinarytrees an expression tree from a postfix expression string.

        Args:
            string: A string representing a postfix expression.

        Returns:
            The root position of the construct expression tree.
        """
        s = []
        for ch in string:
            if ch in "+-*/":
                rightchild = s.pop()
                leftchild = s.pop()
                s.append(ExpressionTree(ch, leftchild, rightchild))
            else:
                s.append(ExpressionTree(ch))

        self.root = s.pop().getRoot()
        return self.root


#driver code
if __name__ == "__main__":
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    test = ExpressionTree()
    test.constructbinarytree("ab+c/d*e+f-")
    print(test)
