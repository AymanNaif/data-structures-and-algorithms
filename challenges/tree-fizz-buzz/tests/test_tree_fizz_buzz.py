from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import tree_fizz_buzz, K_ary_tree, Node
import pytest
from tree_fizz_buzz import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_fizz_buzz_expected_output(tree):
    actual = tree_fizz_buzz(tree)
    expected = ['2', '7', 'Fizz', '2', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', '4']
    assert actual == expected


def test_fizz_buzz_fail():
    k_tree = K_ary_tree()
    actual = tree_fizz_buzz(k_tree)
    expected = "Tree is Empty"
    assert actual == expected


@pytest.fixture
def tree():
    k_tree = K_ary_tree()
    k_tree.root = Node(2)
    k_tree.root.children += [Node(7)]
    k_tree.root.children += [Node(6)]
    k_tree.root.children += [Node(2)]
    k_tree.root.children += [Node(5)]
    k_tree.root.children += [Node(15)]
    k_tree.root.children += [Node(5)]
    k_tree.root.children += [Node(9)]
    k_tree.root.children += [Node(4)]
    return k_tree
