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
        if value in self.node_lst:
            return True
        else:
            return False

    def __str__(self):
        # "{ a } -> { b } -> { c } -> NULL"
        # Loop over all nodes
        # print all values in one line
        strr = ''
        for x in range(len(self.node_lst)):
            if x == 0:
                strr += ' ' + str((self.node_lst[x])) + ' -> '
            elif x == len(self.node_lst)-1:
                strr += str((self.node_lst[x])) + '  -> NULL '
            else:
                strr += str((self.node_lst[x])) + ' -> '

        # strr += 'NULL '
        return strr

    def __repr__(self):
        return 'Nothing'


if __name__ == "__main__":
    # Instances of Node
    n1 = Node(34)
    # n2 = Node('Suhaib')
    n3 = Node(True)

    ll = LinkedList()
    # Value of first node on head
    ll.append(4)
    # next of head (next of Node(4)) is Null
    ll.append(-1)
    ll.append('s')
    ll.insert('ayman')
    # print(ll.include('ayman'))
    # print(ll.include('test'))
    # # I have ll: head - Node(4) -> Node(-1) -> Node('s') -> None
    # print(ll.head.value)
    # print(ll.head.next.value)
    # print(ll.head.next.next.value)
    # print(ll.head.next.next.next.value)
    print(ll.__str__())
