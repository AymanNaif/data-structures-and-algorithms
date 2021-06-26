class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        try:
            """
            a function that return the tree as root >> left >> right
            """
            if not self.root:
                return "the tree is empty!"
            else:
                output = []

                def order_tree(node):
                    nonlocal output
                    output += [node.value]
                    if node.left:
                        order_tree(node.left)
                    if node.right:
                        order_tree(node.right)
                    return output
                return order_tree(self.root)
        except:
            print("something went wrong please try again")

    def in_order(self):
        """
            a function that return the tree as left >> root >> right
        """
        try:
            if not self.root:
                return "the tree is empty!"
            else:
                output = []

                def order_tree(node):
                    if node.left:
                        order_tree(node.left)
                    nonlocal output
                    output += [node.value]
                    if node.right:
                        order_tree(node.right)
                    return output
                return order_tree(self.root)
        except:
            print("something went wrong please try again")

    def post_order(self):
        """
            a function that return the tree as left >> right >> root
        """
        try:
            if not self.root:
                return "the tree is empty!"
            else:
                output = []

                def order_tree(node):
                    if node.left:
                        order_tree(node.left)
                    if node.right:
                        order_tree(node.right)
                    nonlocal output
                    output += [node.value]
                    return output
                final_out = order_tree(self.root)
                return final_out
        except:
            print("something went wrong please try again")


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        """
        to add a new value to the tree 
        """
        try:
            if not self.root:
                self.root = Node(value)
            else:
                node = self.root
                while node:
                    if node.value > value:
                        if not node.left:
                            node.left = Node(value)
                            break
                        node = node.left
                    else:
                        if not node.right:
                            node.right = Node(value)
                            break
                        node = node.right
        except:
            print("something went wrong please try again")

    def contains(self, value):
        """
        function return true if the tree contain the value or value not found 
        """
        try:
            if not self.root:
                return 'The Tree is empty'
            else:
                node = self.root
                while node:
                    if node.value == value:
                        return True
                    if node.value > value:
                        if not node.left:
                            return 'The value is not in the Tree'
                        node = node.left
                    else:
                        if node.right == None:
                            return 'The value is nor in the Tree'
                        node = node.right
        except:
            print("something went wrong please try again")
