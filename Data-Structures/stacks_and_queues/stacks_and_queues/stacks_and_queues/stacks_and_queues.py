from inspect import stack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,):
        self.top = None

    def push(self, item):

        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            # raise ValueError('empty stack')
            return 'empty stack'
        else:
            self.top = self.top.next

    def peek(self):
        if self.is_empty():
            # raise ValueError('empty stack')
            return 'empty stack'

        else:
            return self.top.value

    def is_empty(self):
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            node.next = self.rear
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            # raise ValueError('empty queue') NOTE : I don't know how to expected it on test file
            return 'empty queue'
        else:

            self.front = None
            current = self.rear

            while current.next != None:

                current = current.next
                self.front = current

    def is_empty(self):
        return self.rear == None

    def peek(self):
        return self.front.value


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)

    actual = queue.dequeue()
    print(actual)
