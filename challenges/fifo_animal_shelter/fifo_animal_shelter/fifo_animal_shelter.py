class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def __str__(self):

        strr = ''
        current = self.front
        while current is not None:
            if current.next is None:
                strr = strr + f'[{current.value}]'
                current = current.next
            else:
                strr = strr + f'[{current.value}]->'
                current = current.next

        return strr


class AnimalShelter:
    cat = Queue()
    dog = Queue()

    def __init__(self):
        pass

    def __str__(self):
        result = self.dog.__str__()
        result += self.cat.__str__()
        return result

    def enqueue(self, name, type):
        if type == 'dog':
            self.dog.enqueue(name)
        elif type == 'cat':
            self.cat.enqueue(name)
        else:
            return 'you can just choose dog or cat'

    def dequeue(self, type=None):
        if type == 'dog':
            return self.dog.dequeue()
        elif type == 'cat':
            return self.cat.dequeue()
        else:
            return 'you can just choose dog or cat'
