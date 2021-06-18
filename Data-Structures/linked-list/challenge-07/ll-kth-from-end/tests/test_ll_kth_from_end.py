from ll_kth_from_end import __version__
from ll_kth_from_end.ll_kth_from_end import LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_k_greater():
    ll = LinkedList()
    ll.append('test')
    ll.append('hii')
    ll.insert('hisai')
    ll.insertBefore('test', 'wow')
    ll.insertAfter('hii', 55)
    print(ll.node_lst)
    actual = ll.kthFromEnd(10)
    excepted = 'out of index'
    assert actual == excepted


def test_k_same_length():
    ll = LinkedList()
    ll.append('test')
    ll.append('hii')
    ll.insert('hisai')
    ll.insertBefore('test', 'wow')
    ll.insertAfter('hii', 55)
    print(ll.node_lst)
    actual = ll.kthFromEnd(5)
    excepted = 'out of index'
    assert actual == excepted


def test_k_same_length():
    ll = LinkedList()
    ll.append('test')
    ll.append('hii')
    ll.insert('hisai')
    ll.insertBefore('test', 'wow')
    ll.insertAfter('hii', 55)
    actual = ll.kthFromEnd(-1)
    excepted = 55
    assert actual == excepted


def test_with_size_1_1():
    ll = LinkedList()
    ll.append('test')
    actual = ll.kthFromEnd(0)
    excepted = 'test'
    assert actual == excepted


def test_with_size_1_2():
    ll = LinkedList()
    ll.append('test')
    actual = ll.kthFromEnd(4)
    excepted = 'out of index'
    assert actual == excepted


def test_with_size_1_3():
    ll = LinkedList()
    ll.append('test')
    actual = ll.kthFromEnd(-2)
    excepted = 'out of index'
    assert actual == excepted


def test_happy_path():
    ll = LinkedList()
    ll.append('test')
    ll.append('hii')
    ll.insert('hisai')
    ll.insertBefore('test', 'wow')
    ll.insertAfter('hii', 55)
    actual = ll.kthFromEnd(2)
    excepted = 'test'
    assert actual == excepted
