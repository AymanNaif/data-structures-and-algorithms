from tree_fizz_buzz.stack_and_queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class K_ary_tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root:
            arr = [self.root.value]
            arr += [child.value for child in self.root.children]
            return str(arr)
        else:
            return "Tree is Empty"


def tree_fizz_buzz(k_ary_tree):
    if not k_ary_tree.root:
        return "Tree is Empty"

    values = []
    queue = Queue()

    if k_ary_tree:
        queue.enqueue(k_ary_tree.root)

    while not queue.isEmpty():

        tree = queue.dequeue()

        if tree.value % 3 == 0 and tree.value % 5 == 0:
            tree.value = 'FizzBuzz'
            values += [tree.value]
        elif tree.value % 3 == 0:
            tree.value = 'Fizz'
            values += [tree.value]
        elif tree.value % 5 == 0:
            tree.value = 'Buzz'
            values += [tree.value]
        else:
            values += [str(tree.value)]

        for child in tree.children:
            queue.enqueue(child)

    return values
