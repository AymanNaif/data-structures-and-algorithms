from stacks_and_queues import Queue

class Node:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, data=None):
        if data:
            data = Node(data)
        self.root = data

    @staticmethod
    def breadth_first(tree, node=None, array=None):

        q = Queue()

        if not array:
            array = []

        if tree.root:
            q.enqueue(tree.root)

        while q.peek():

            front_node = q.dequeue()

            array.append(front_node.data)

            if front_node.left:
                q.enqueue(front_node.left)

            if front_node.right:
                q.enqueue(front_node.right)

        return array

    def post_order(self, node=None, result=[]):
        
        node = node or self.root

        if node.left:
            self.post_order(node.left, result)

        if node.right:
            self.post_order(node.right, result)

        result.append(node.data)

        return result

    def pre_order(self, node=None, result=[]):
        
        node = node or self.root
        result.append(node.data)

        if node.left:
            self.pre_order(node.left, result)

        if node.right:
            self.pre_order(node.right, result)

        return result

    def in_order(self, node=None, result=[]):
        
        node = node or self.root
        
        if node.left:
            self.in_order(node.left, result)

        result.append(node.data)

        if node.right:
            self.in_order(node.right, result)

        return result

class BinarySearchTree(BinaryTree):
    def __init__(self, data=None):
        super().__init__(data)

    def add(self, data):

        node = Node(data)

        if not self.root:
            self.root = node

            return

        current = self.root

        while True:
            if node.data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = node

                    return

            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node

                    return

    def contains(self, data):

        if not self.root:
            return False

        current = self.root

        while True:
            if data == current.data:
                
                return True

            if data < current.data:
                if current.left:
                    current = current.left
                else:

                    return False

            else:
                if current.right:
                    current = current.right
                else:

                    return False