from trees import __version__

from trees.tree import BinaryTree, Node, BinarySearchTree


def test_empty_tree():
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_tree_single_node():
    tree = BinarySearchTree()
    tree.add('A')
    actual = tree.root.value
    expected = 'A'
    assert actual == expected


def test_add_left_right():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    result = [tree.root.left.value, tree.root.right.value]
    actual = result
    expected = [9, 11]
    assert actual == expected


def test_pre_order():
    tree = BinarySearchTree()
    tree.add('A')
    tree.add('B')
    tree.add('C')
    actual = tree.pre_order()
    excepted = ['A', 'B', 'C']
    assert actual == excepted


def test_in_order():
    tree = BinarySearchTree()
    tree.add('A')
    tree.add('B')
    tree.add('C')
    actual = tree.in_order()
    excepted = ['A', 'B', 'C']
    assert actual == excepted


def test_post_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    actual = tree.post_order()
    excepted = [9, 11, 10]
    assert actual == excepted


def test_max_value():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(20)
    tree.add(9)
    tree.add(11)
    tree.add(5)
    assert tree.maximum_value() == 20
