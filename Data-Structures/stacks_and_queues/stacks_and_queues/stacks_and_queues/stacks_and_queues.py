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
            pop_item = self.top
            self.top = self.top.next
        return pop_item.value

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
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            return 'empty queue'
        else:
            dequeue_value = self.front
            self.front = self.front.next
            dequeue_value.next = None
            return dequeue_value.value

    def is_empty(self):
        return self.rear == None

    def peek(self):
        return self.front.value


if __name__ == "__main__":
    queue_test = Queue()
    queue_test.enqueue(8)
    queue_test.enqueue('hi')
    queue_test.enqueue(-4)
    queue_test.enqueue(6)
    queue_test.dequeue()
    queue_test.dequeue()

    print(queue_test.dequeue())
    # print(queue.front.value)
    # queue.dequeue()
