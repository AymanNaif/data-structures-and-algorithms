from asserts.ll_kth_from_end import *


def zipLists(list1, list2):
    """
    take two linked lists and return one zip linked list
    """
    current1 = list1.head
    current2 = list2.head
    while current1:
        if current2:
            store1 = current1.next
            current1.next = current2

            if store1:
                store2 = current2.next
                current2.next = store1

            if not store2:
                break

            current1 = store1
            current2 = store2
    return list1


if __name__ == '__main__':
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
    print(actual)
