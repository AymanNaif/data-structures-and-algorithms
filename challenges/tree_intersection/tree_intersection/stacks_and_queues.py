class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    top = None

    def __init__(self, top=None):
        self.top = top

    def push(self, val):
        new_node = Node(val)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):

        if not self.is_empty():
            self.top = self.top.next_node
            temp = self.top
            return temp.data

        return None

    def peek(self):

        if not self.is_empty():
            return self.top.data

        return None

    def is_empty(self):
        if self.top == None:
            return True

        return False


class Queue:

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def peek(self):
        if not self.is_empty():
            return self.front.data

        return None

    def dequeue(self):
        if not self.is_empty():
            self.front = self.front.next_node
            temp = self.front
            temp.next = None
            return temp.data

        return None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def is_empty(self):

        if self.front == None:
            return True

        return False
