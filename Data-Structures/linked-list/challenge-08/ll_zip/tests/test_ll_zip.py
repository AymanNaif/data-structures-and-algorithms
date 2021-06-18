from ll_zip import __version__
from ll_zip.ll_zip import LinkedList, zipLists


def test_version():
    assert __version__ == '0.1.0'


def test_zip_one():
    ll_one = LinkedList()
    ll_one.append('test')
    ll_one.append(5)
    ll_one.append(7)
    ll_one.append(8)
    ll_one.append(9)

    ll_two = LinkedList()
    ll_two.append('two')
    ll_two.append(0)
    ll_two.append('a')
    ll_two.append(23)
    ll_two.append('k')
    actual = zipLists(ll_one, ll_two)
    excepted = '{ test } -> { two } -> { 5 } -> { 0 } -> { 7 } -> { a } -> { 8 } -> { 23 } -> { 9 } -> { k } -> Null'
    assert actual == excepted


def test_zip_two():
    ll_one = LinkedList()
    ll_one.append('test')
    ll_one.insert(5)
    ll_one.append(7)
    ll_one.insertBefore(7, 8)
    ll_one.append(9)

    ll_two = LinkedList()
    ll_two.append('two')
    ll_two.append(0)
    ll_two.append(23)
    ll_two.insertAfter(23, 'a')
    ll_two.append('k')
    actual = zipLists(ll_one, ll_two)
    excepted = '{ 5 } -> { two } -> { test } -> { 0 } -> { 8 } -> { 23 } -> { 7 } -> { a } -> { 9 } -> { k } -> Null'
    assert actual == excepted


def test_zip_three():
    ll_one = LinkedList()
    ll_one.append('hi')
    ll_one.insert(5)
    ll_one.append(7)
    ll_one.insertBefore(8, 5)
    ll_one.append("ayman")

    ll_two = LinkedList()
    ll_two.append('y')
    ll_two.insert('a')
    ll_two.append('m')
    ll_two.insertAfter('m', 'a')
    ll_two.append('n')
    actual = zipLists(ll_one, ll_two)
    excepted = '{ 5 } -> { a } -> { hi } -> { y } -> { 7 } -> { m } -> { 5 } -> { a } -> { ayman } -> { n } -> Null'
    assert actual == excepted
