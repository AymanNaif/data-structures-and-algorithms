from typing import Counter


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Draft:
ll: head - None
ll.append(4)
ll: head - Node(4) -> None
ll.append(-1)
ll: head - Node(4) -> Node(-1) -> None
ll.append('s')
ll: head - Node(4) -> Node(-1) -> Node('s') -> None
"""


class LinkedList:
    def __init__(self):
        self.node_lst = []
        self.head = None

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.node_lst.insert(0, self.head.value)
        else:
            current = self.head
            self.head = node
            node.next = current
            self.node_lst.insert(0, self.head.value)

    def append(self, value):
        """
        Adds a node of a value to the end of LL
        """

        node = Node(value)
        if not self.head:
            self.head = node
            self.node_lst.append(self.head.value)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            self.node_lst.append(current.next.value)

    def include(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        if self.head == None:
            return False
        else:
            current = self.head
            while current != None:
                if current.value == value:
                    return True
                else:
                    current = current.next
            return False

    def insertBefore(self, value, new_value):
        """
        add Node before specific one
        """
        current = self.head
        node = Node(new_value)
        if current.value == value:
            node.next = current
            current = node
            self.node_lst.insert(current)
        counter = 0
        while current.next is not None:
            counter = counter+1
            if current.next.value == value:
                break
            current = current.next

        node.next = current.next
        current.next = node
        self.node_lst.insert(counter, current.next.value)

        return self.__str__()

    def insertAfter(self, value, new_value):
        """
        add Node After specific one
        """
        current = self.head
        node = Node(new_value)
        counter = 0
        while current != None:
            counter = counter+1
            if current.value == value:
                break
            current = current.next

        node.next = current.next
        current.next = node
        self.node_lst.insert(counter, current.next.value)

        return self.__str__()

    def kthFromEnd(self, k):
        """
        takes a number (k) as a parameter.
        Return the node’s value that is k from the end of the linked list
        """
        if k >= len(self.node_lst):
            return 'out of index'
        elif k < 0:
            if (k*-1) > len(self.node_lst):
                return 'out of index'
            else:
                for idx, i in enumerate(self.node_lst):
                    if idx == k+len(self.node_lst):
                        return i
        else:
            for idx, i in enumerate(self.node_lst[::-1]):
                if idx == k:
                    return i

    def __str__(self):

        strr = ''
        current = self.head
        while current is not None:
            strr = strr + f'{{ { current.value } }} -> '
            current = current.next
        else:
            strr = strr + 'Null'
        return strr

    def __repr__(self):
        return 'Nothing'
