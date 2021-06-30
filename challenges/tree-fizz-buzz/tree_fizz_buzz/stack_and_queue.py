
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
        if self.front == None:
            self.front = node
            self.rear = node

        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            raise Exception('Error!')

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        try:
            if self.front == None:
                raise Exception

            return self.front.value

        except Exception:
            return 'Error!'

    def isEmpty(self):
        return self.front == None

    def __str__(self):
        arr = []
        while not self.isEmpty():
            arr.append(self.dequeue().value)

        return str(arr)
