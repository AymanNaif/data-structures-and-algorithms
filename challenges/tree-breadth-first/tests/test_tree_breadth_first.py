from tree_breadth_first import __version__
from tree_breadth_first.tree_breadth_first import breadth_first
from tree_breadth_first.tree import BinaryTree, Node


def test_version():
    assert __version__ == '0.1.0'


def test_breadth_first():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = breadth_first(tree)
    assert expected == actual
