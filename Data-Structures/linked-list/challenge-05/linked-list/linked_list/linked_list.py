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

    def append(self, value):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(value)
        if not self.head:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def include(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        if self.head is None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                else:
                    current = current.next
            return False

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
