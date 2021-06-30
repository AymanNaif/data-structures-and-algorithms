from .stack_and_queue import Queue


def breadth_first(tree):

    if not tree:
        return "Tree is Empty"

    lst_val = []
    queue = Queue()

    if tree:
        queue.enqueue(tree.root)

    while not queue.isEmpty():

        tree_node = queue.dequeue()
        lst_val += [tree_node.value]

        if tree_node.left:
            queue.enqueue(tree_node.left)

        if tree_node.right:
            queue.enqueue(tree_node.right)

    return lst_val
